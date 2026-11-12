from django.core.paginator import Paginator
from django.db.models.aggregates import Count
from django.shortcuts import render

from .models import Category, Product


# Create your views here.
def categories_index(request):
    queryset = Category.objects.annotate(product_count=Count('products')).order_by('-id')
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)

    return render(request, "pages/categories/index.dj.html", {"categories": categories})


def products_index(request):
    queryset = Product.objects.select_related("category").order_by("-id")
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(request, "pages/products/index.dj.html", {"products": products})
