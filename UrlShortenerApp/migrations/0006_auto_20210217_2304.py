# Generated by Django 3.1.5 on 2021-02-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortenerApp', '0005_auto_20210205_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='new_short_url',
            field=models.URLField(max_length=60, verbose_name='Сокращенная ссылка'),
        ),
    ]
