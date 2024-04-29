from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from pytils.translit import slugify

# Create your views here.
from blogg.models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content',)
    success_url = reverse_lazy('blogg:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content',)
    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogg:view', args=[self.kwargs.get('pk')])


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset = None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogg:list')