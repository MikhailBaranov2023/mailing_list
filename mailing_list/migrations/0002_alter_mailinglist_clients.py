# Generated by Django 4.2.4 on 2023-08-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglist',
            name='clients',
            field=models.ManyToManyField(blank=True, null=True, to='mailing_list.client', verbose_name='клиенты'),
        ),
    ]
