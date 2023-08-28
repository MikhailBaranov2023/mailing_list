from django.contrib import admin
from mailing_list.models import MailingList, Client


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'finish_time', 'status', 'periodicity',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
