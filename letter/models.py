from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Letter(models.Model):
    subject = models.TextField(default='')
    message = models.TextField(default='')
    sent_time = models.DateTimeField(default=datetime.datetime.now)
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE) 
