from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer


# Create your views here.
def index(req):
    data = {
        "msg": "Hello, World!",
    }
    return JsonResponse(data)


def car_list_view(req):
    cars = Carlist.objects.all()
    data = {"cars": list(cars.values())}
    return JsonResponse(data)


def car_detail_view(req, id):
    car = Carlist.objects.get(id=id)
    data = {"name": car.name, "description": car.description, "active": car.active}
    return JsonResponse(data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
