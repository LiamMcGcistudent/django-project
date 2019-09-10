from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from datetime import datetime
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products.html", {"products": products})
    
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    
    return render(request, "product_detail.html", {"product": product})