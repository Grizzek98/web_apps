from django.urls import path
from . import views

# allows you to declare the URL that each view can 
# be found at

urlpatterns = [
    path("", views.startle_dreams_index, name = "startle_dreams_index"),
    path("form/", views.startle_dreams_form, name = "startle_dreams_form")
]