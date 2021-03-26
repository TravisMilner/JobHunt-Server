from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from JobHuntapi.models import Company


class AllCompanies(ViewSet):

    def create(self, request):

        company = Company()

        company.name = request.data['name']
        company.notes = request.data['notes']
        company.user = Token.objects.get(user = request.auth.user)

        try:
            company.save()
            serializer = CompanySerializer(company, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({'reason': ex.message}, status = status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):

        try:
            company = Company.objects.get(pk=pk)

            serializer = CompanySerializer(company, context = {"request": request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        companies = Company.objects.filter(user=request.auth)

        serializer = CompanySerializer(companies, many = True, context = {'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):

        company= Company.objects.get(pk=pk)
        company.name = request.data['name']
        company.notes = request.data['notes']
        company.user = Token.objects.get(user = request.auth.user)

        company.save()

        return Response({}, status = status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            company = Company.objects.get(pk=pk)
            company.delete()

            return Response({}, status = status.HTTP_204_NO_CONTENT)

        except Company.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)












class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'notes', 'user')
