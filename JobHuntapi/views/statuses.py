from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from JobHuntapi.models import Status

class AllStatuses(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            status = Status.objects.get(pk=pk)

            serializer = StatusSerializer(status, context = {'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        statuses = Status.objects.all()

        serializer = StatusSerializer(statuses, many = True, context = {'request': request})

        return Response(serializer.data)


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'label')