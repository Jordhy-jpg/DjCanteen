from django.urls import path

from .views import categories_index

urlpatterns = [path("", categories_index, name="categories_index")]
