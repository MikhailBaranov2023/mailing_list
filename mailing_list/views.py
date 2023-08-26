from django.views.generic import ListView, CreateView, DeleteView, DetailView
from mailing_list.models import MailingList
from django.urls import reverse_lazy
from mailing_list.forms import FormMailingList
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class MailingListView(LoginRequiredMixin, ListView):
    model = MailingList


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'mailing_list.add_mailinglist'
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

