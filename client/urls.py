from django.contrib import admin
from django.urls import path, include
from client.apps import ClientConfig
from client.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDetailView, ClientDeleteView

app_name = ClientConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list'),
    path('create/', ClientCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='edit'),
    path('view/<int:pk>', ClientDetailView.as_view(), name='view'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='delete'),
]
