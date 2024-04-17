from django.shortcuts import render

from main.models import Product


# Create your views here.

# def index(request):
#     return render(request, 'main/index.html')

def index(request):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
        'title': 'Main page',
    }
    return render(request, 'main/index.html', context)


def products(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Product page',
    }
    return render(request, 'main/products.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Человечек {name} "
              f"ввел свой номер телефона {phone} "
              f"с таким сообщением {message}")
    context = {
            'title': 'Contacts',
        }
    return render(request, 'main/contacts.html', context)
