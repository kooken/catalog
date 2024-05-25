from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from main.forms import ProductForm, VersionForm, ProductModeratorForm
from main.models import Product, Version


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']
        for product in products:
            active_version = product.version.filter(active_version=True).first()
            product.active_version = active_version
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    success_url = reverse_lazy('main:index')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.product_name)
            new_post.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.product_name)
            new_post.save()

        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('main.can_edit_product_description') and user.has_perm('main.can_edit_is_published'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Человечек {name} "
              f"ввел свой номер телефона {phone} "
              f"с таким сообщением {message}")
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contacts'
        return context


class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):
        return Version.objects.filter(product=Product.objects.get(pk=self.kwargs.get('pk')))


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        if form.is_valid():
            product_pk = self.kwargs.get("pk")
            product = get_object_or_404(Product, pk=product_pk)
            form.instance.product = product
        return super().form_valid(form)

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('main:index')

class VersionDetailView(DetailView):
    model = Version
    # context_object_name = 'versions'

class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('main:index')