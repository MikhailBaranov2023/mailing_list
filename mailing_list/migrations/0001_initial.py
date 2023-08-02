# Generated by Django 4.2.4 on 2023-08-02 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='время рассылки')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'завершена'), (2, 'создана'), (3, 'запушена')], default=2, verbose_name='статус рассылки')),
                ('periodicity', models.PositiveSmallIntegerField(choices=[(1, 'раз в день'), (2, 'раз в неделю'), (3, 'раз в месяц')], default=2, verbose_name='периодичность')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
    ]
