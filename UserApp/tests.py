from django.http import HttpRequest
from django.test import TestCase, Client
from django.urls import resolve
from UrlShortenerApp.views import CreateUrlView, statistic_about_url
from .models import User


def testuser_login_for_test():
    user = User.objects.create(username='testuser')
    user.set_password('testuserpassword')
    user.save()
    cur_client = Client()
    login_successful = cur_client.login(username="testuser", password="testuserpassword")
    return cur_client, login_successful


class HomePageTest(TestCase):

    def test_root_is_a_create_url_page(self):
        found = resolve('/')  # преобразование URL адреса и нахождение функции/класса представления
        self.assertEqual(found.view_name, CreateUrlView.__module__ + '.' + CreateUrlView.__name__)

    def test_root_is_main_page(self):
        response = self.client.get('/')  # тестовый клиент, вместо создания HttpRequest
        self.assertTemplateUsed(response, 'UrlShortenerApp/create_url.html')


class StatPageTest(TestCase):

    def test_statistic_page_html(self):
        cur_client, login_successful = testuser_login_for_test()
        self.assertTrue(login_successful)
        response = cur_client.get('http://127.0.0.1:8000/urls/stat/11')
        self.assertTemplateUsed(response, 'UrlShortenerApp/statistic.html')


class UserTests(TestCase):

    def test_user_create(self):
        us = User()
        us.username = "test_1"
        us.set_password("testpassword2021")
        us.save()
        user_from_db = User.objects.get(username="test_1")
        self.assertTrue(isinstance(user_from_db, User))
