from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Letter(models.Model):
    subject = models.TextField(default='')
    message = models.TextField(default='')
    write_time = models.DateTimeField(default=timezone.now)
    destination_time = models.DateTimeField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    letter_status = ( ('Readed', 'Readed'), ('Not Read', 'Not Read') )
    status = models.CharField(
             max_length=8,
             choices=letter_status,
             default='Not Read',
             )
    email_status = (('sent', 'sent'), ('not sent', 'not sent'))
    email_sent = models.CharField(
                 max_length=8,
                 choices=email_status,
                 default='not sent',
                 )

