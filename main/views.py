from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} {email}: {message}")
    return render(request, 'main/index.html')

def contacts(request):
    return render(request, 'main/contacts.html')