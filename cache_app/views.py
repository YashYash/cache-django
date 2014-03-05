from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


# @cache_page(900)
def index(request):
    data = {"request": request}
    return render(request, "index.html", data)