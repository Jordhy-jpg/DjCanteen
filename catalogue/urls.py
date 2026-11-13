from django.urls import path

from .views import (
    add_category,
    add_product,
    categories_index,
    categories_show,
    details_show,
    products_index,
)

urlpatterns = [
    path("", categories_index, name="categories_index"),
    path("categories/<int:category_id>/", categories_show, name="categories_show"),
    path("categories/add/", add_category, name="add_category"),
    path("products/index/", products_index, name="products_index"),
    path("products/add/", add_product, name="add_product"),
    path("products/<int:product_id>/", details_show, name="details_show"),
]
