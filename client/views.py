from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from client.models import Client
from django.urls import reverse_lazy


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('client:list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('client:list')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')
