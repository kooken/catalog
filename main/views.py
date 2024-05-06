from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from main.forms import ProductForm, VersionForm
from main.models import Product, Version


# Create your views here.

# def index(request):
#     return render(request, 'main/product_list.html')

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']  # Получаем список продуктов из контекста

        # Для каждого продукта получаем данные об активной версии
        for product in products:
            active_version = product.version.filter(active_version=True).first()
            # Добавляем информацию об активной версии в контекст для каждого продукта
            product.active_version = active_version

        return context

# class ProductListView(ListView):
#     model = Product
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Получаем объект Product, который отображается на странице
#         product = self.get_object()
#         # Получаем связанную с продуктом активную версию
#         active_version = Version.objects.filter(product=product, active_version=True).first()
#         # Добавляем информацию о версии в контекст страницы
#         context['active_version'] = active_version
#         return context

    # def get_context_data(self,*args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     products = Product.objects.all()
    #
    #     for product in products:
    #         versions = Version.objects.filter(product=product)
    #         active_version = versions.filter(active_version=True)
    #         if active_version:
    #             product.version_name = active_version.last().version_name
    #             product.version_no = active_version.last().version_no
    #     context_data['object_list'] = products
    #     return context_data

# class ProductListView(ListView):
#     model = Product
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#         products = Product.objects.all()
#
#         for product in products:
#             versions = Version.objects.filter(product=product)
#             active_versions = versions.filter(active_version=True)
#             if active_versions:
#                 product.active_version = active_versions.last().version_name
#             else:
#                 product.active_version = 'Нет активной версии'
#
#         context_data['object_list'] = products
#         return context_data

# def index(request):
#     products_list = Product.objects.all()
#     context = {
#         'products_list': products_list,
#         'title': 'Main page',
#     }
#     return render(request, 'main/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('main:index')

# def products(request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'title': 'Product page',
#     }
#     return render(request, 'main/product_detail.html', context)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('product_name', 'product_description', 'product_image', 'product_price', 'product_category',)
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.product_name)
            new_post.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('product_name', 'product_description', 'product_image', 'product_price', 'product_category',)
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.product_name)
            new_post.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:index')


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

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f"Человечек {name} "
#               f"ввел свой номер телефона {phone} "
#               f"с таким сообщением {message}")
#     context = {
#             'title': 'Contacts',
#         }
#     return render(request, 'main/contacts.html', context)


class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):
        # queryset = Version.objects.all()
        # products = Product.objects.all()
        # for product in products:
        #     print(product)
        #     versions = Version.objects.filter(product=product)
        #     print(queryset.product == product)
        #     return versions
        return Version.objects.filter(product=Product.objects.get(pk=self.kwargs.get('pk')))


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        # Получаем pk продукта из URL
        product_pk = self.kwargs.get("pk")

        # Проверяем, существует ли продукт с этим pk
        product = get_object_or_404(Product, pk=product_pk)

        # Добавляем связанный продукт к форме перед сохранением
        form.instance.product = product

        if form.is_valid():
            new_version = form.save()
            new_version.slug = slugify(new_version.version_name)
            new_version.save()

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