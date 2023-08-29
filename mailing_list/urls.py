from django.contrib import admin
from django.urls import path, include
from mailing_list.apps import MailingListConfig
from mailing_list.views import HomeView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDeleteView, MailingSettingsUpdateView, \
    MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingClintListView, toggle_client

app_name = MailingListConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='main'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('settings/', MailingSettingsListView.as_view(), name='mailing_list'),
    path('settings/create/', MailingSettingsCreateView.as_view(), name='mailing_create'),
    path('settings/edit/<int:pk>/', MailingSettingsUpdateView.as_view(), name='mailing_edit'),
    path('settings/delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='meiling_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('settings/<int:pk>/client_list', MailingClintListView.as_view(), name='mailing_client'),
    path('settings/<int:pk>/clients/<int:client_pk>', toggle_client, name='mailing_client_toggle'),
]
