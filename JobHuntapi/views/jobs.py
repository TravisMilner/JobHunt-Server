from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from JobHuntapi.models import Job
from JobHuntapi.models import Status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AllJobs(ViewSet):

    def create(self, request):

        


        job = Job()

        job.name = request.data['name']
        job.date_of_app = request.data['date_of_app']
        job.status = Status.objects.get(pk = request.data['status'])
        job.notes = request.data['notes']
        job.link = request.data['link']
        job.user = Token.objects.get(user = request.auth.user)

        try:
            job.save()
            serializer = JobSerializer(job, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status = status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):

        try:

            job = Job.objects.get(pk=pk)

            serializer = JobSerializer(job, context = {'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)


    def list(self, request):

        jobs = Job.objects.filter(user=request.auth)


        serializer = JobSerializer(jobs, many=True, context={'request': request})
        return Response(serializer.data)


    
    def update(self, request, pk=None):

        job = Job.objects.get(pk=pk)
        job.name = request.data['name']
        job.date_of_app = request.data['date_of_app']
        job.status = Status.objects.get(pk=request.data['status'])
        job.notes= request.data['notes']
        job.link = request.data['link']
        job.user = Token.objects.get(user = request.auth.user)

        job.save()

        return Response({}, status = status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk=None):

        try:
            job = Job.objects.get(pk=pk)
            job.delete()

            return Response({}, status= status.HTTP_204_NO_CONTENT)

        except Job.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status= status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    














class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'name', 'date_of_app', 'status', 'notes', 'link', 'user')
        depth = 1