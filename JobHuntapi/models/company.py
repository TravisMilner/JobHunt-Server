from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    notes = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)