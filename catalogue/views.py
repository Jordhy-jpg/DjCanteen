from django.shortcuts import render


# Create your views here.
def categories_index(request):
    return render(request, "views/pages/categories/index.dj.html")
