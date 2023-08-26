from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField(verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='коментарий', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
