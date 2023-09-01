from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, ProfileView, generate_new_password, activate_new_user, UsersListView, toggle_activity
from django.views.decorators.cache import cache_page, never_cache

app_name = UsersConfig.name
template_name = 'users/login.html'

urlpatterns = [
    path('', never_cache(LoginView.as_view(template_name=template_name)), name='login'),
    path('logout/', never_cache(LogoutView.as_view()), name='logout'),
    path('register/', never_cache(RegisterView.as_view()), name='register'),
    path('profile/', never_cache(ProfileView.as_view()), name='profile'),
    path('profile/genpassword/', never_cache(generate_new_password), name='generate_new_password'),
    path('activate/<int:pk>/', never_cache(activate_new_user), name='activate'),
    path('list/', cache_page(60)(UsersListView.as_view()), name="list"),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
