from django.urls import path

from .views import categories_index, products_index

urlpatterns = [
    path("", categories_index, name="categories_index"),
    path("products/index/", products_index, name="products_index"),
]
