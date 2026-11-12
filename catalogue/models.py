from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")

class Detail(models.Model):
    calories = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.TextField(null=True, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="details")