from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from UserApp.models import User
from PetProject.settings import SITE_BASE_URL
import string
import random
from datetime import date, timedelta


class ShortenedUrl(models.Model):
    user_creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Создатель ссылки",
                                     related_name="urls", null=True)
    original_url = models.URLField(max_length=300, verbose_name="Оригинальная ссылка")
    new_short_url = models.URLField(max_length=50, verbose_name="Сокращенная ссылка")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-pk']

    def save(self, user=None, original_url=None):
        if not user or not original_url:  # обновление записи, не создание новой
            self.user_creator = self.user_creator
            self.original_url = self.original_url
        else:  # создание новой записи
            if isinstance(user, User):
                self.user_creator = user
            else:
                self.user_creator = User.objects.get(pk=1)
            self.original_url = original_url
            self.new_short_url = ShortenedUrl.get_shortened_url()
        super(ShortenedUrl, self).save()

    @staticmethod
    def get_shortened_url():
        while True:
            generated_suffix = ""
            for i in range(10):
                generated_suffix += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)

            new_url_existence = ShortenedUrl.objects.filter(new_short_url=SITE_BASE_URL + generated_suffix)
            if not new_url_existence:
                return SITE_BASE_URL + generated_suffix

    @staticmethod
    def get_full_url_from_requested(request):
        request_url = request.get_full_path()
        final_url = SITE_BASE_URL + request_url[1:]
        try:
            original_URL_fromDB = ShortenedUrl.objects.get(new_short_url=final_url)
            return original_URL_fromDB
        except ObjectDoesNotExist:
            return HttpResponseNotFound('<h1>Страница не найдена, проверьте адрес :(</h1>')

    def change_active_status(self):

        if self.is_active:
            self.is_active = False
            self.save()
            return 'profile_url'
        else:
            self.is_active = True
            self.save()
            return 'hidden_urls_url'


class UrlClick(models.Model):
    related_url = models.ForeignKey(ShortenedUrl, on_delete=models.PROTECT, verbose_name="Соответствующая ссылка",
                                    related_name='clicks')
    click_date = models.DateField(auto_now_add=True, null=True)

    def __init__(self, related_url=None, *args):
        super(UrlClick, self).__init__(*args)
        if isinstance(related_url, ShortenedUrl):
            self.related_url = related_url
            self.save()

    @staticmethod
    def get_statistic_for_url(url_for_stat):
        all_clicks = UrlClick.objects.filter(related_url=ShortenedUrl(pk=url_for_stat)).count()
        delta = timedelta(days=1)
        today = date.today()
        list_of_30_days = [today - delta * i for i in range(30)]  # 30 предыдущих дней начиная с сегодняшнего
        full_stat = {datestring: len(count_of_clicks) for
                     datestring, count_of_clicks in
                     zip(
                         list_of_30_days,
                         [UrlClick.objects.filter(
                             related_url=ShortenedUrl(pk=url_for_stat),
                             click_date=day
                         ) for day in list_of_30_days
                         ]
                     )
                     }
        return full_stat.items()
