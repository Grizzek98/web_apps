from django.urls import path
from . import views

urlpatterns = [
    path("", views.startle_dreams_index, name = "startle_dreams_index"),
    path("form/", views.startle_dreams_form, name = "startle_dreams_form")
]