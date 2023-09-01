from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page, never_cache

from mailing_list.apps import MailingListConfig
from mailing_list.views import HomeView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDeleteView, MailingSettingsUpdateView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingClintListView, toggle_client, \
    MailingLogListView, ContactsTemplateView

app_name = MailingListConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='main'),

    path('clients/', cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('clients/create/', never_cache(ClientCreateView.as_view()), name='client_create'),
    path('clients/edit/<int:pk>/', never_cache(ClientUpdateView.as_view()), name='client_edit'),
    path('clients/delete/<int:pk>/', never_cache(ClientDeleteView.as_view()), name='client_delete'),

    path('settings/', cache_page(60)(MailingSettingsListView.as_view()), name='mailing_list'),
    path('settings/create/', never_cache(MailingSettingsCreateView.as_view()), name='mailing_create'),
    path('settings/edit/<int:pk>/', never_cache(MailingSettingsUpdateView.as_view()), name='mailing_edit'),
    path('settings/delete/<int:pk>/', never_cache(MailingSettingsDeleteView.as_view()), name='meiling_delete'),

    path('message/', cache_page(60)(MessageListView.as_view()), name='message_list'),
    path('message/create/', never_cache(MessageCreateView.as_view()), name='message_create'),
    path('message/edit/<int:pk>/', never_cache(MessageUpdateView.as_view()), name='message_edit'),
    path('message/delete/<int:pk>/', never_cache(MessageDeleteView.as_view()), name='message_delete'),

    path('settings/<int:pk>/client_list', cache_page(60)(MailingClintListView.as_view()), name='mailing_client'),
    path('settings/<int:pk>/clients/<int:client_pk>', never_cache(toggle_client), name='mailing_client_toggle'),

    path('mailinglogs/', cache_page(60)(MailingLogListView.as_view()), name='mailing_logs'),
    path('contacts/', cache_page(60)(ContactsTemplateView.as_view()), name='contacts'),
]
