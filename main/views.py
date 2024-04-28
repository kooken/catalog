from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from main.models import Product


# Create your views here.

# def index(request):
#     return render(request, 'main/product_list.html')

class ProductListView(ListView):
    model = Product

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
