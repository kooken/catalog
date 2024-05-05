from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, VersionDeleteView, VersionListView, VersionUpdateView, VersionDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='update_version'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='version_detail'),
]
