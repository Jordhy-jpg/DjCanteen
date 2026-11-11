from django.contrib import admin

from catalogue.models import Category, Detail, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Detail)
