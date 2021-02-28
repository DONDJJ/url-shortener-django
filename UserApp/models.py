from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to="avatars/", verbose_name="user_image")


# Create your models here.



