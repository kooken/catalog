from django.urls import path

from main.apps import MainConfig
from main.views import index, contacts, products

app_name = MainConfig.name

urlpatterns= [
    path('', index, name='index'),
    path('products/<int:pk>', products, name='products'),
    path('contacts/', contacts, name='contacts'),
]