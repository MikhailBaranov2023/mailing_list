from django.db import models
from django.contrib.auth.models import AbstractUser
from mailing_list.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    telegram = models.CharField(max_length=50, verbose_name='телеграм', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
