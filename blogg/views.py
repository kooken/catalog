from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from pytils.translit import slugify
from django.core.mail import send_mail

# Create your views here.
from blogg.models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'is_published', 'preview',)
    success_url = reverse_lazy('blogg:list')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'is_published', 'preview',)
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

    @staticmethod
    def send_notification(title, views_count):
        send_mail(
            subject='Blog',
            message=f'Ваша статья {title} достигла {views_count} просмотров!',
            from_email="koooken@yandex.ru",
            recipient_list=["metmaria23@gmail.com"]
        )

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count >= 2:
            self.send_notification(self.object.title, self.object.views_count)

        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogg:list')

