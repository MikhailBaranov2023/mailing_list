from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from blog.models import Blog
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import Http404
from pytils.translit import slugify


class BlogListView(ListView):
    model = Blog


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if not self.request.user.has_perm('blog.add_blog'):
            raise Http404
        return self.object

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
    permission_required = 'blog.delete_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if not self.request.user.has_perm('blog.delete_blog'):
            raise Http404
        return self.object


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')
    permission_required = 'blog.change_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if not self.request.user.has_perm('blog.change_blog'):
            raise Http404
        return self.object

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
            self.kwargs['slug'] = new_mat.slug

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('slug')])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object
