from django.db import models
from UserApp.models import User
from PetProject.settings import SITE_BASE_URL
import string
import random


# Create your models here.
class ShortenedUrl(models.Model):
    user_creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Создатель ссылки",
                                     related_name="urls", null=True)
    original_url = models.URLField(max_length=300, verbose_name="Оригинальная ссылка")
    new_short_url = models.URLField(max_length=50, verbose_name="Сокращенная ссылка")

    class Meta:
        ordering = ['-pk']

    def save(self, user, original_url):
        self.user_creator = user
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


class UrlClick(models.Model):
    pass
