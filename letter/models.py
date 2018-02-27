from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Letter(models.Model):
    subject = models.TextField(default='')
    message = models.TextField(default='')
<<<<<<< HEAD
    sent_time = models.DateTimeField(default=timezone.now)
    datetime = models.DateTimeField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
=======
    write_time = models.DateTimeField(default=timezone.now)
    destination_time = models.DateTimeField()
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    letter_status = ( ('Readed', 'Readed'), ('Not Read', 'Not Read') )
    status = models.CharField(
             max_length=8,
             choices=letter_status,
             default='Not Read',
             )

>>>>>>> db07ea120c33d466c899e1f13cbd5aa5244fdda9
