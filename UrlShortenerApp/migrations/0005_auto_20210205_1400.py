# Generated by Django 3.1.5 on 2021-02-05 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlShortenerApp', '0004_auto_20210205_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlclick',
            name='click_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
