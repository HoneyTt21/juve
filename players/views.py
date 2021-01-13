from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from . import models

# Create your views here.
def home_view(request):
    return render(
        request,
        "pages/players/home.html",
        context={
        },
    )