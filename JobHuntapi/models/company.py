from django.db import models
from rest_framework.authtoken.models import Token

class Company(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=500)
    user = models.ForeignKey(Token, on_delete=models.CASCADE)