# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_supplier/', views.add_supplier, name='add_supplier'),
]
# wholesale_inventory_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path( include('inventory.urls')),
]
