from django.core.management.base import BaseCommand, CommandError
from letter.models import Letter
from django.utils import timezone
from django.core.mail import send_mass_mail, send_mail

class Command(BaseCommand):
    help = 'Send Email'
    def handle(self, *args, **options):

        letter_list = Letter.objects.filter(destination_time__lte=timezone.now(), 
                email_sent='not sent')
    
        email_list = []
        for letter in letter_list:
            email_list.append((letter.subject, 
                letter.message, 
                letter.user.email, 
                [letter.user.email]))
            letter.email_sent = 'sent'
            letter.save()
        send_mass_mail(email_list, fail_silently=False)

