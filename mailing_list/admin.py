from django.contrib import admin
from mailing_list.models import MailingSettings, Client, MailingClient, MailingLog, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'email', 'owner')
    list_filter = ('name',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'finish_time', 'status', 'periodicity', 'message', 'owner')
    list_filter = ('status',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title_message', 'body_message', 'owner',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('last_attempt', 'status', 'mailing_service_response', 'client', 'mailing', 'owner',)
    list_filter = ('status',)


@admin.register(MailingClient)
class MailingClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'client', 'mailing', 'owner')
    list_filter = ('client',)
