from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from client.models import Client
from django.urls import reverse_lazy
from client.forms import ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'client.add_client'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:list')


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    permission_required = 'client.change_client'
    success_url = reverse_lazy('client:list')


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'client.view_client'
    model = Client


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')

    def test_func(self):
        return self.request.user.is_superuser
