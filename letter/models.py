from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Letter(models.Model):
    subject = models.TextField(default='')
    message = models.TextField(default='')
    sent_time = models.DateTimeField(default=timezone.now)
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE) 
