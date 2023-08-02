from django.contrib import admin
from mailing_list.models import MailingList


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'periodicity',)
