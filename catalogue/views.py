from django.shortcuts import render

from .models import Category


# Create your views here.
def categories_index(request):
    categories = Category.objects.all().order_by("-id")
    return render(request, "pages/categories/index.dj.html", {"categories": categories})
