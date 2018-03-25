# Generated by Django 2.0.1 on 2018-03-22 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('letter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(default='')),
                ('message', models.TextField(default='')),
                ('write_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Readed', 'Readed'), ('Not Read', 'Not Read')], default='Not Read', max_length=8)),
                ('email_sent', models.CharField(choices=[('sent', 'sent'), ('not sent', 'not sent')], default='not sent', max_length=8)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='letter',
            name='reciever',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='letter',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]