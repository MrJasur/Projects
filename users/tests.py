from urllib import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user

# Create your tests here.
class RegistrTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(reverse('users:register'), 
        data={
            "username":"coder",
            "first_name":"Jasurbek",
            "last_name":"Odilov",
            "email":"abc@gmail.com",
            "password":"1202abc",
        }
        )

        user = User.objects.get(username='coder')

        self.assertEqual(user.first_name, "Jasurbek")
        self.assertEqual(user.last_name, "Odilov")
        self.assertEqual(user.email, "abc@gmail.com")
        self.assertNotEqual(user.password, "1202abc")
        self.assertTrue(user.check_password('1202abc'))

    def test_register_page_status_code(self):
        response = self.client.get(reverse('users:register'))
        self.assertEquals(response.status_code, 200)

    def test_required_fields(self):
        response = self.client.post(reverse('users:register'),
        data = {
            'first_name':'Jasurbek',
            'email': 'abc@gmail.com',
        })
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')


    def test_invalid_email(self):
        response = self.client.post(reverse('users:register'),
        data = {
            "username":"coder",
            "first_name":"Jasurbek",
            "last_name":"Odilov",
            "email":"invalid",
            "password":"1202abc",
        })
        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_unique_username(self):
        user = User.objects.create(username = 'coder', first_name = 'Jasurbek')
        user.set_password('1202abc')
        user.save()

        response = self.client.post(reverse('users:register'),
        data = {
            "username":"coder",
            "first_name":"Jasurbek",
            "last_name":"Odilov",
            "email":"abcd@gmail.com",
            "password":"1202abc",
        })
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')


class LoginTestCase(TestCase):
    def test_successful_login(self):
        user=User.objects.create(username='coder', first_name='Jasurbek')
        user.set_password('abc123')
        user.save()

        self.client.post(
            reverse('users:login'),
            data = {
                'username':'coder',
                'password':'abc123'
            }
        )

        user=get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):
        user = User.objects.create(username='coder')
        user.set_password('abc123')
        user.save()

        self.client.post(
            reverse('users:login'),
            data={
                'username':'coder2',
                'password':'1bc123'
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

        user = User.objects.create(username='coder3')
        user.set_password('abc123')
        user.save()

        self.client.post(
            reverse('users:login'),
            data={
                'username':'coder3',
                'password':'abc1234'
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)