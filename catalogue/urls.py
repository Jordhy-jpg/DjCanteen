from django.urls import path

from .views import add_category, add_product, categories_index, products_index

urlpatterns = [
    path("", categories_index, name="categories_index"),
    path("products/index/", products_index, name="products_index"),
    path("categories/add/", add_category, name="add_category"),
    path("products/add/", add_product, name="add_product"),
]
