from django import forms

from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input w-full mt-1",
                    "placeholder": "Category Name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea w-full mt-1",
                    "placeholder": "Category Description",
                }
            ),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "description", "price", "stock"]
        widgets = {
            "category": forms.Select(attrs={"class": "select w-full"}),
            "name": forms.TextInput(
                attrs={
                    "class": "input w-full mt-1",
                    "placeholder": "Product Name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea w-full mt-1",
                    "placeholder": "Product Description",
                }
            ),
            "price": forms.NumberInput(),
            "stock": forms.NumberInput(),
        }
