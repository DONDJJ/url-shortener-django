from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from UrlShortenerApp.views import CreateUrlView, statistic_about_url


class HomePageTest(TestCase):

    def test_root_is_a_create_url_page(self):
        found = resolve('/')  # преобразование URL адреса и нахождение функции/класса представления
        self.assertEqual(found.view_name, CreateUrlView.__module__ + '.' + CreateUrlView.__name__)


class StatPageTest(TestCase):

    def test_statistic_page_html(self):
        request = HttpRequest()
        response = statistic_about_url(request, 3)  # <class 'django.http.response.HttpResponse'>
        html = response.content.decode('utf8')  # изначально это нули и единицы
        self.assertTrue(html.startswith("\n\n<!DOCTYPE html>"))
        self.assertIn("<title>Подробнее</title>", html)
        self.assertTrue(html.endswith("</html>"))

