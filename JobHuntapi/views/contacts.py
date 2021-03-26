from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from JobHuntapi.models import Contact

class AllContacts(ViewSet):

    def create(self, request):

        contact = Contact()

        contact.name = request.data['name']
        contact.company = request.data['company']
        contact.email = request.data['email']
        contact.phone_number = request.data['phone_number']
        contact.notes = request.data['notes']
        contact.user = Token.objects.get(user = request.auth.user)

        try:
            contact.save()
            serializer = ContactSerializer(contact, context= {'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({'reason': ex.message}, status = status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):

        try: 
            contact = Contact.objects.get(pk=pk)
            serializer = ContactSerializer(contact, context = {'request': request})

            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):

        contacts = Contact.objects.filter(user=request.auth)

        serializer= ContactSerializer(contacts, many= True, context = {'reqeust': request})
        return Response(serializer.data)

    def update(self, request, pk= None):
        contact = Contact.objects.get(pk=pk)

        contact.name = request.data['name']
        contact.company = request.data['company']
        contact.email = request.data['email']
        contact.phone_number = request.data['phone_number']
        contact.notes = request.data['notes']
        contact.user = Token.objects.get(user= request.auth.user)

        contact.save()

        return Response({}, status= status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):

        try:
            contact = Contact.objects.get(pk=pk)
            contact.delete()

            return Response({}, status = status.HTTP_204_NO_CONTENT)

        except Contact.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        









class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'name', 'company', 'email', 'phone_number', 'notes', 'user')
        