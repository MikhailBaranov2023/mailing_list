from django.contrib import admin
from django.urls import path, include
from mailing_list.apps import MailingListConfig
from mailing_list.views import MailingListView, MailingCreateView, MailingDeleteView, MailingDetailView, \
    ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView, ClientListView, MailingUpdateView

app_name = MailingListConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='list'),
    path('create/', MailingCreateView.as_view(), name='create'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>', MailingUpdateView.as_view(), name='update'),
    path('view/<int:pk>', MailingDetailView.as_view(), name='view'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('client/view/<int:pk>', ClientDetailView.as_view(), name='client_view'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
