# Generated by Django 2.0.1 on 2018-03-19 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0007_auto_20180226_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='email_sent',
            field=models.CharField(choices=[('sent', 'sent'), ('not sent', 'not sent')], default='not sent', max_length=8),
        ),
    ]
