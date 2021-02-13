from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse
from . import forms, models

# Create your views here.

from django.shortcuts import render
from . import models

# Create your views here.
def home_view(request):
    return render(
        request,
        "pages/players/home.html",
        context={},
    )


class AddView(FormView):
    template_name = "pages/players/add.html"
    form_class = forms.AddPlayerForm

    def form_valid(self, form):
        form.save()
        return super(AddView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("player:home")