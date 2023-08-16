from django.contrib import admin
from django.urls import path, include
from mailing_list.apps import MailingListConfig
from mailing_list.views import MailingListView, MailingCreateView, MailingDeleteView

app_name = MailingListConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('delete/<int:pk>>', MailingDeleteView.as_view(), name='delete'),
]
