from django.shortcuts import render

from .models import Category, Product


# Create your views here.
def categories_index(request):
    categories = Category.objects.all().order_by("-id")
    return render(request, "pages/categories/index.dj.html", {"categories": categories})

def products_index(request):
    products = Product.objects.all().order_by("-id")
    return render(request, "pages/products/index.dj.html", {"products": products})