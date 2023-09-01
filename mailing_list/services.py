from django.core.mail import send_mail
from django.conf import settings
import datetime
from smtplib import SMTPException
from mailing_list.models import MailingSettings, MailingLog


def _send_email(message_settings, message_client):
    result_txt = ('Усешно отправлена')
    try:
        result = send_mail(
            subject=message_settings.message.title_message,
            message=message_settings.message.body_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[message_client.client.email],
            fail_silently=False
        )
    except SMTPException:
        result_txt = ('Ошибка отправки')

    MailingLog.objects.create(
        status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
        mailing=message_settings,
        client_id=message_client.client_id,
        mailing_service_response=result_txt
    )


def send_mails():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)
    for mailing_settings in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):
        if (datetime_now > mailing_settings.start_time) and (datetime_now < mailing_settings.finish_time):
            for mailing_client in mailing_settings.mailingclient_set.all():
                mailing_log = MailingLog.objects.filter(
                    client=mailing_client.client,
                    mailing=mailing_settings
                )
                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_attempt').first().last_attempt

                    if mailing_settings.periodicity == MailingSettings.PERIOD_DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            _send_email(mailing_settings, mailing_client)
                        elif mailing_settings.periodicity == MailingSettings.PERIOD_WEEKLY:
                            if (datetime_now - last_try_date).days >= 7:
                                _send_email(mailing_settings, mailing_client)
                        elif mailing_settings.periodicity == MailingSettings.PERIOD_MONTHLY:
                            if (datetime_now - last_try_date).days >= 30:
                                _send_email(mailing_settings, mailing_client)
                else:
                    _send_email(mailing_settings, mailing_client)
