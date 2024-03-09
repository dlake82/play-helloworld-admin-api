from django.urls import path
from rest_framework import routers
from user import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.car_list_view, name="car_list"),
]
