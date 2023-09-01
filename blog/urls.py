from django.urls import path
from blog.views import BlogListView, BlogCreateView, BlogDeleteView, BlogUpdateView, BlogDetailView
from blog.apps import BlogConfig
from django.views.decorators.cache import cache_page, never_cache

app_name = BlogConfig.name

urlpatterns = [
    path('', cache_page(60)(BlogListView.as_view()), name='list'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('delete/<slug:slug>/', never_cache(BlogDeleteView.as_view()), name='delete'),
    path('edit/<slug:slug>/', never_cache(BlogUpdateView.as_view()), name='edit'),
    path('view/<slug:slug>/', cache_page(60)(BlogDetailView.as_view()), name='view'),

]
