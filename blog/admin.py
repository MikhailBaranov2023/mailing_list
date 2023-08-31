from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'articles', 'image', 'view_count', 'data')
    list_filter = ('title',)

# Register your models here.
