from django.urls import path
from . import views

urlpatterns = [
    path("", views.startle_dreams_index, name = "startle_dreams_index")
]