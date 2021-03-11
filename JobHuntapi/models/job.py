from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    name = models.CharField(max_length=200)
    date_of_app = models.DateField(auto_now = False, auto_now_add= False)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    notes = models.CharField(max_length= 255)
    link = models.URLField(max_length=500, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)