from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView, CreateView

from mailing_list.models import MailingSettings, Client, Message, MailingClient, MailingLog
from mailing_list.forms import MessageForm, MailingSettingsForm, ClientForm, MailingSettingsForManagerForm


class HomeView(TemplateView):
    template_name = 'mailing_list/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count_mailing'] = MailingSettings.objects.all().count()
        context_data['count_mailing_active'] = MailingSettings.objects.filter(
            status=3).count()
        context_data['count_unique_customers'] = Client.objects.distinct().count()
        context_data['title'] = 'Главная страница рассылок'
        return context_data


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'mailing_list/client_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.view_client'):
            return queryset
        return queryset.filter(owner=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing_list/client_form.html'
    success_url = reverse_lazy('mailing_list:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailing_list/client_form.html'
    success_url = reverse_lazy('mailing_list:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'mailing_list/client_confirm_delete.html'
    success_url = reverse_lazy('mailing_list:client_list')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалить чужого клиента """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MailingSettingsListView(LoginRequiredMixin, ListView):
    model = MailingSettings
    template_name = 'mailing_list/mailinglist_list.html'

    def get_queryset(self):
        """Пользователь видит только свои рассылки"""
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.view_mailingsettings'):
            return queryset  # Если есть право доступа, то пользователь видит все рассылки
        return queryset.filter(owner=self.request.user)


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing_list/mailinglist_form.html'
    success_url = reverse_lazy('mailing_list:mailing_list')

    def form_valid(self, form):
        """ У рассылки появляется 'owner' - авторизированный пользователь """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing_list/mailinglist_form.html'
    success_url = reverse_lazy('mailing_list:mailing_list')


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    template_name = 'mailing_list/mailinglist_confirm_delete.html'
    success_url = reverse_lazy('mailing_list:mailing_list')
    permission_required = 'mailing_list.change_mailingsettings'

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалять чужое сообщение """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mailing_list/message_list.html'

    def get_queryset(self):
        """Пользователь видит только свои сообщения"""
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing.view_mailingmessage'):
            return queryset  # Если есть право доступа, то пользователь видит все сообщения
        return super().get_queryset().filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing_list/message_form.html'
    success_url = reverse_lazy('mailing_list:message_list')

    def form_valid(self, form):
        """ У сообщения появляется 'owner' - авторизированный пользователь """
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing_list/message_form.html'
    success_url = reverse_lazy('mailing_list:message_list')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может менять чужое сообщение """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = ''
    success_url = reverse_lazy('mailing_list:message_list')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалять чужое сообщение """
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MailingClintListView(ListView):
    model = MailingClient
    template_name = 'mailing_list/mailingclient_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(mailing=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['clients'] = Client.objects.filter(owner=self.request.user)
        context_data['mailing_pk'] = self.kwargs.get('pk')

        return context_data


def toggle_client(request, pk, client_pk):
    if MailingClient.objects.filter(client_id=client_pk, mailing_id=pk).exists():
        MailingClient.objects.filter(client_id=client_pk, mailing_id=pk).delete()
    else:
        MailingClient.objects.create(client_id=client_pk, mailing_id=pk)
    return redirect(reverse('mailing_list:mailing_client', args=[pk]))


class MailingLogListView(ListView):
    model = MailingLog

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('mailing_list.view_mailinglog'):
            return queryset
        return queryset.filter(owner=self.request.user)
