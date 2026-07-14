from django.urls import include, path

from authentication.views.login import LoginAPIView
from authentication.views.logout import LogoutAPIView
from authentication.views.refresh import RefreshTokenAPIView

api_router = [
    path("login", LoginAPIView.as_view(), name="auth_api_login"),
    path("logout", LogoutAPIView.as_view(), name="auth_api_logout"),
    path("refresh", RefreshTokenAPIView.as_view(), name="auth_api_refresh"),
]

urlpatterns = [
    path("api/", include(api_router)),
]
