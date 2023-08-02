from django.views.generic import ListView, CreateView, DeleteView
from mailing_list.models import MailingList
from django.urls import reverse_lazy


class MailingListView(ListView):
    model = MailingList


class MailingCreateView(CreateView):
    model = MailingList
    fields = ('date', 'status', 'periodicity', 'title_message', 'body_message')
    success_url = reverse_lazy('mailing_list:list')


class MailingDeleteView(DeleteView):
    model = MailingList
    success_url = reverse_lazy('mailing_list:list')
