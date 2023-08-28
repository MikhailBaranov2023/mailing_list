from django.core.mail import send_mail
from django.conf import settings
import datetime
from mailing_list.models import Client, MailingList


def check_mailing(mailing_settings):
    datetime_now = datetime.datetime.now()
    if mailing_settings.status == 3:
        if mailing_settings.start_time == datetime_now:
            return True
        return False
    return False


def send_mailing(mailing_settings):
    if check_mailing(mailing_settings) == True:
        send_mail(
            subject=mailing_settings.title_message,
            message=mailing_settings.body_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=mailing_settings.clients.email,
        )
