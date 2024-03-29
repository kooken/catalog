from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Человечек {name} ввел свой номер телефона {phone} с таким сообщением {message}")
    return render(request, 'main/contacts.html')