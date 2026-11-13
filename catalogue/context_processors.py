from .forms import CategoryForm


def navbar_forms(request):
    return {"category_form": CategoryForm()}
