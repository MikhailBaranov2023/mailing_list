from django.db import models
from client.models import Client

MAILING_STATUS = [(1, 'завершена'), (2, 'создана'), (3, 'запушена')]
MAILING_PERIODICITY = [(1, 'раз в день'), (2, 'раз в неделю'), (3, 'раз в месяц')]
NULLABLE = {'blank': True, 'null': True}


class MailingList(models.Model):
    date = models.DateTimeField(verbose_name='время рассылки')
    status = models.PositiveSmallIntegerField(default=2, choices=MAILING_STATUS, verbose_name='статус рассылки')
    periodicity = models.PositiveSmallIntegerField(default=2, choices=MAILING_PERIODICITY, verbose_name='периодичность')

    title_message = models.CharField(max_length=200, verbose_name='тема письма', **NULLABLE)
    body_message = models.TextField(verbose_name='письмо', **NULLABLE)

    clients = models.ManyToManyField(Client, verbose_name='клиенты')

    def __str__(self):
        return f'Тема:{self.title_message}, Письмо: {self.body_message}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
