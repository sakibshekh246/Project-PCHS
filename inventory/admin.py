# inventory/admin.py
from django.contrib import admin
from .models import Product, Supplier

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'supplier')

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
