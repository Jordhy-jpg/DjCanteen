from django.shortcuts import render


# Create your views here.
def categories_index(request):
    return render(request, "pages/categories/index.dj.html")
