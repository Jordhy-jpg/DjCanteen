from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "input w-full mt-1.5",
                "placeholder": "Category Name",
            }),
            "description": forms.Textarea(attrs={
                "class": "textarea w-full mt-4",
                "placeholder": "Category Description",
            }),
        }
