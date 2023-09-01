import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import User
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy, reverse
from users.forms import UserRegisterForm, UserProfileForm
from users.services import verification


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        verification(user)
        return super().form_valid(form)


def activate_new_user(request, pk):
    user = get_user_model()
    user_for_activate = user.objects.get(id=pk)
    user_for_activate.is_active = True
    user_for_activate.save()
    return render(request, 'users/email_verification.html')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль - {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))


class UsersListView(LoginRequiredMixin, ListView):
    model = User


def toggle_activity(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True

    user.save()

    return redirect(reverse('users:list'))
