# Generated by Django 2.2.5 on 2021-01-28 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlClick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=300, verbose_name='Оригинальная ссылка')),
                ('new_short_url', models.URLField(max_length=50, verbose_name='Сокращенная ссылка')),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='urls', to=settings.AUTH_USER_MODEL, verbose_name='Создатель ссылки')),
            ],
        ),
    ]
