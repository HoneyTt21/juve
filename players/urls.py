from django.urls import path
from . import views

app_name = "player"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("add", views.AddView.as_view(), name="add")
]