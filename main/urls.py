from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView

app_name = MainConfig.name

urlpatterns= [
    path('', ProductListView.as_view(), name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),

]