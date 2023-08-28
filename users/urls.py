from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, ProfileView, generate_new_password, activate_new_user

app_name = UsersConfig.name
template_name = 'users/login.html'

urlpatterns = [
    path('', LoginView.as_view(template_name=template_name), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('activate/<int:pk>/', activate_new_user, name='activate'),

]
