from django.db import models
from rest_framework.authtoken.models import Token

class Contact(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    notes = models.CharField(max_length=300)
    user = models.ForeignKey(Token, on_delete=models.CASCADE)