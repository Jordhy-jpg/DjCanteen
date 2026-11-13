from .forms import CategoryForm, ProductForm


def navbar_forms(request):
    return {"category_form": CategoryForm(), "product_form": ProductForm()}
