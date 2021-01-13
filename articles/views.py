from django.shortcuts import render
from . import models

# Create your views here.
def home_view(request):
    return render(
        request,
        "pages/articles/home.html",
        context={
        },
    )