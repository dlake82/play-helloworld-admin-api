from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from .views import RefreshView, LoginView, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(), name="token_obtain_pair"),
    path("refresh/", RefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="blacklist"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
]
