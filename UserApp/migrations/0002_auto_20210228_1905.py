# Generated by Django 3.1.5 on 2021-02-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='user_image'),
        ),
    ]
