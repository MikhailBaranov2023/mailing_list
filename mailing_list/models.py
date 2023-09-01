from django.db import models
import datetime
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField(verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='коментарий', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='пользователь')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title_message = models.CharField(max_length=200, verbose_name='тема письма', **NULLABLE)
    body_message = models.TextField(verbose_name='письмо', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='пользователь')

    def __str__(self):
        return f'{self.body_message}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailingSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'

    STATUSES = (
        (STATUS_CREATED, 'Создана'),
        (STATUS_STARTED, 'Запущена'),
        (STATUS_DONE, 'Завершена'),
    )
    start_time = models.DateTimeField(verbose_name='время начала', default=datetime.datetime.now(datetime.timezone.utc))
    finish_time = models.DateTimeField(verbose_name='время окончания',
                                       default=datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                                           days=7))
    status = models.CharField(max_length=20, default=STATUS_CREATED, choices=STATUSES, verbose_name='статус рассылки')
    periodicity = models.CharField(max_length=20, default=PERIOD_DAILY, choices=PERIODS, verbose_name='периодичность')

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='пользователь')

    def __str__(self):
        return f'{self.start_time}/ {self.periodicity}'

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )
    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время посденей попытки')
    status = models.CharField(default=STATUS_OK, choices=STATUSES, verbose_name='статус попытки')
    mailing_service_response = models.TextField(verbose_name='Ответ почтового сервиса', **NULLABLE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='Рассылка')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='пользователь')

    def __str__(self):
        return f'{self.last_attempt} - {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'


class MailingClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    mailing = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='пользователь')

    def __str__(self):
        return f'{self.client} - {self.mailing}'

    class Meta:
        verbose_name = 'Список рассылки'
        verbose_name_plural = 'Список рассылок'
