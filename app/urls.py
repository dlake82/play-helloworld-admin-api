from django.contrib import admin
from django.urls import path, include

from django.urls import include, path
from rest_framework import routers

from user import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("snippets/", include("snippets.urls")),
]

urlpatterns += router.urls
