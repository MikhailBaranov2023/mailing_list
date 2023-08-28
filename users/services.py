from django.core.mail import send_mail
from django.conf import settings


def verification(user):
    send_mail(subject='Активация',
              message=f'Для активации профиля пройдите по ссылке - http://127.0.0.1:8000/users/activate/{user.id}/',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[user.email])
