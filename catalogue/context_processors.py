from .forms import CategoryForm, DetailForm, ProductForm


def navbar_forms(request):
    return {
        "category_form": CategoryForm(),
        "product_form": ProductForm(),
        "detail_form": DetailForm(),
    }
