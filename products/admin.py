from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdminFields(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'description', 'added', 'price')

admin.site.register(Product, ProductAdminFields)