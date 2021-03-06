from django.urls import resolve
from django.test import TestCase
from letter.views import homepage
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from letter.models import Letter
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

# Create your unittests here.

class HomepageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_uses_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

class RegisterAndLoginTest(TestCase):

    def test_user_can_register_account(self):
        user = User.objects.create_user(username='test_user',email='test@ema.il',password='test_password')
        user = authenticate(username='test_user', password='test_password')
        if user is None:
            raise AssertionError('cannot create user account')

    def test_register_form_use_correct_template(self):
        self.client.post('/letter/register', data={'regis_username': 'test_user',
                                                              'regis_email': 'test@ema.il',
                                                              'regis_password': 'test_password'})
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_redirect_after_register(self):
        response = self.client.post('/letter/register', data={'regis_username': 'test_user',
                                                              'regis_email': 'test@ema.il',
                                                              'regis_password': 'test_password'})
        self.assertRedirects(response, '/')

    def test_shows_username_in_title_after_register(self):
        self.client.post('/letter/register', data={'regis_username': 'test_user',
                                                              'regis_email': 'test@ema.il',
                                                              'regis_password': 'test_password'})
        response = self.client.get('/')
        self.assertContains(response, 'test_user')

    def test_login_form_use_correct_template(self):
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_redirect_after_login(self):
        user = User.objects.create_user(username='test_user',email='test@ema.il',password='test_password')
        response = self.client.post('/letter/login', data={'login_username': 'test_user',
                                                           'login_password': 'test_password'})
        self.assertRedirects(response, '/')

    def test_shows_username_in_title_after_login(self):
        user = User.objects.create_user(username='test_user',email='test@ema.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user',
                                                           'login_password': 'test_password'})
        response = self.client.get('/')
        self.assertContains(response, 'test_user')

class LetterModelTest(TestCase):

    def test_create_and_retrieve_letter(self):
        first_user_ = User.objects.create_user(username='first_user',
                email='first@ema.il',password='first_password')
        first_datetime_ = timezone.now() + timezone.timedelta(hours=1)

        second_user_ = User.objects.create_user(username='second_user',
                email='second@ema.il', password='second_password')
        second_datetime_ = timezone.now() + timezone.timedelta(hours=2)

        Letter.objects.create(subject='first_subject', 
                message='first_message', destination_time=first_datetime_, user=first_user_)
        Letter.objects.create(subject='second_subject', 
                message='second_message', destination_time=second_datetime_, user=second_user_)
        Letter.objects.create(subject='first_subject',
                message='first_message', datetime=first_datetime_, user=first_user_)
        Letter.objects.create(subject='second_subject',
                message='second_message', datetime=second_datetime_, user=second_user_)

        saved_letters= Letter.objects.all()
        self.assertEqual(saved_letters.count(), 2)

        first_letter = saved_letters[0]
        second_letter = saved_letters[1]

        self.assertEqual(first_letter.subject, 'first_subject')
        self.assertEqual(first_letter.message, 'first_message')
        self.assertEqual(format(first_letter.destination_time, '%d/%m/%Y %H:%M'), 
                format(first_datetime_, '%d/%m/%Y %H:%M'))
        self.assertEqual(first_letter.user, first_user_)

        self.assertEqual(second_letter.subject, 'second_subject')
        self.assertEqual(second_letter.message, 'second_message')
        self.assertEqual(format(second_letter.destination_time, '%d/%m/%Y %H:%M'), 
                format(second_datetime_, '%d/%m/%Y %H:%M'))
        self.assertEqual(second_letter.user, second_user_)

class LetterViewTest(TestCase):

    def test_uses_write_letter_template(self):
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})

        response = self.client.get('/letter/write/')
        self.assertTemplateUsed(response, 'write_letter.html')

    def test_new_letter_test(self):
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})

        datetime_ = timezone.now() + timezone.timedelta(hours=2)

        self.client.post('/letter/send', data={'subject': 'test_subject',
            'message': 'test_message', 'datetime': format(datetime_, '%d/%m/%Y %H:%M')})
        saved_letters= Letter.objects.all()
        self.assertEqual(saved_letters.count(), 1)

        saved_letter = saved_letters[0]
        self.assertEqual(saved_letter.subject, 'test_subject')
        self.assertEqual(saved_letter.message, 'test_message')
        self.assertEqual(format(saved_letter.destination_time, '%d/%m/%Y %H:%M'), format(datetime_, '%d/%m/%Y %H:%M'))
        self.assertEqual(saved_letter.user, user)


class HistoryViewTest(TestCase):

    def test_uses_history_template(self):
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})

        response = self.client.get('/letter/history')
        self.assertTemplateUsed(response, 'history.html')

    def test_multiple_user_letters_display_in_history(self):
        user_ = User.objects.create_user(username='test_user',
                email='test@ema.il',password='test_password')
        datetime_1 = timezone.now() + timezone.timedelta(hours=1)
        datetime_2 = timezone.now() + timezone.timedelta(hours=2)

        another_user_ = User.objects.create_user(username='another_user',
                email='another@ema.il', password='another_password')
        datetime_3 = timezone.now() + timezone.timedelta(hours=3)
        datetime_4 = timezone.now() + timezone.timedelta(hours=4)

        Letter.objects.create(subject='user_subject1',
                message='user_message1', destination_time=datetime_1, user=user_)
        Letter.objects.create(subject='user_subject2',
                message='user_message2', destination_time=datetime_2, user=user_)

        Letter.objects.create(subject='another_subject1',
                message='another_message1', destination_time=datetime_3, user=another_user_)
        Letter.objects.create(subject='another_subject2',
                message='another_message2', destination_time=datetime_4, user=another_user_)

        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})
        response = self.client.get('/letter/history')

        self.assertContains(response, 'user_subject1')
        self.assertNotContains(response, 'user_message1')
        self.assertContains(response, 'user_subject2')
        self.assertNotContains(response, 'user_message2')

        self.assertNotContains(response, 'another_subject1')
        self.assertNotContains(response, 'user_message1')
        self.assertNotContains(response, 'another_subject2')
        self.assertNotContains(response, 'user_message2')

class inbox_test(TestCase):

    def test_uses_inbox_template(self):
        # create user and login
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})

        # redirect to '/letter/inbox' and check the template
        response = self.client.get('/letter/inbox')
        self.assertTemplateUsed(response, 'inbox.html')

    def test_resolve_past_letter(self):
        # create user and login
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})
        
        # generate past time
        datetime_1 = timezone.now() + timezone.timedelta(hours=-1)
        datetime_2 = timezone.now() + timezone.timedelta(hours=-2)
        
        # write letter with past time
        self.client.post('/letter/send', data={'subject': 'test_subject',
            'message': 'test_message', 'datetime': format(datetime_1, '%d/%m/%Y %H:%M'), 
            'write_time': format(datetime_2, '%d/%m/%Y %H:%M')})

        # count letter form past time
        past_letter = Letter.objects.filter(user=user, destination_time__lte=timezone.now())
        self.assertEqual(past_letter.count(), 1)

        # generate future time
        datetime_1 = timezone.now() + timezone.timedelta(hours=1)
        
        # write letter with future
        self.client.post('/letter/send', data={'subject': 'test_subject',
            'message': 'test_message', 'datetime': format(datetime_1, '%d/%m/%Y %H:%M')})
        
        # past letter must had only 1
        past_letter = Letter.objects.filter(user=user, destination_time__lte=timezone.now())
        self.assertEqual(past_letter.count(), 1)

class read_letter_test(TestCase):

    def test_uses_detail_template(self):
        # create user and login
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})
        
        # generate past time
        datetime_1 = timezone.now() + timezone.timedelta(hours=-1)
        datetime_2 = timezone.now() + timezone.timedelta(hours=-2)

        # write letter with past time
        self.client.post('/letter/send', data={'subject': 'test_subject',
            'message': 'test_message', 'datetime': format(datetime_1, '%d/%m/%Y %H:%M'),
            'write_time': format(datetime_2, '%d/%m/%Y %H:%M')})

        # post letter to '/letter/detail' and check the template
        response = self.client.post('/letter/detail', data={'letter_id': 1})
        self.assertTemplateUsed(response, 'detail.html')

    def test_change_read_status(self):
         # create user and login
        user = User.objects.create_user(username='test_user',email='test@em.il',password='test_password')
        self.client.post('/letter/login', data={'login_username': 'test_user', 'login_password': 'test_password'})

        # generate past time
        datetime_1 = timezone.now() + timezone.timedelta(hours=-1)
        datetime_2 = timezone.now() + timezone.timedelta(hours=-2)

        # write letter with past time
        self.client.post('/letter/send', data={'subject': 'test_subject',
            'message': 'test_message', 'datetime': format(datetime_1, '%d/%m/%Y %H:%M'),
            'write_time': format(datetime_2, '%d/%m/%Y %H:%M')})
        
        # status must be not read
        past_letter = Letter.objects.all()[0]
        self.assertEqual(past_letter.status, 'Not Read')

        # post letter to '/letter/detail'
        response = self.client.post('/letter/detail', data={'letter_id': 1})
        
        # then change status to read
        past_letter = Letter.objects.all()[0]
        self.assertEqual(past_letter.status, 'Read')
        

