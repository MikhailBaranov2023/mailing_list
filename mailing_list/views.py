from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from mailing_list.models import MailingList, Client
from django.urls import reverse_lazy
from mailing_list.forms import FormMailingList, ClientForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class MailingListView(LoginRequiredMixin, ListView):
    model = MailingList


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'mailing_list.add_mailinglist'
    model = MailingList
    form_class = FormMailingList
    success_url = reverse_lazy('mailing_list:list')


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'mailing_list.update_mailinglist'
    model = MailingList
    form_class = FormMailingList
    success_url = reverse_lazy('mailing_list:list')


class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MailingList
    success_url = reverse_lazy('mailing_list:list')

    def test_func(self):
        return self.request.user.is_superuser


class MailingDetailView(DetailView):
    model = MailingList


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'client.add_client'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list:client_list')


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    permission_required = 'client.change_client'
    success_url = reverse_lazy('mailing_list:client_list')


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'client.view_client'
    model = Client


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing_list:client_list')

    def test_func(self):
        return self.request.user.is_superuser
