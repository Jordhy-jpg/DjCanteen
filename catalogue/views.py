from django.core.paginator import Paginator
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse
from django.views.decorators.http import require_http_methods

from catalogue.forms import CategoryForm, ProductForm

from .models import Category, Product


# Create your views here.
def categories_index(request):
    queryset = Category.objects.annotate(product_count=Count("products")).order_by(
        "-id"
    )
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get("page")
    categories = paginator.get_page(page_number)

    return render(request, "pages/categories/index.dj.html", {"categories": categories})


def products_index(request):
    queryset = Product.objects.select_related("category").order_by("-id")
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(request, "pages/products/index.dj.html", {"products": products})


@require_http_methods(["POST"])
def add_category(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        form.save()
        response = HttpResponse()
        response["HX-Location"] = reverse("categories_index")
        return response
    return HttpResponse(form.errors.as_ul())


@require_http_methods(["POST"])
def add_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        response = HttpResponse()
        response["HX-Location"] = reverse("products_index")
        return response
    return HttpResponse(form.errors.as_ul())
