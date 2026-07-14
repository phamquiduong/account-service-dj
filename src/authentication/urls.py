from django.urls import include, path

from authentication.views.login import LoginAPIView

api_router = [
    path("login", LoginAPIView.as_view(), name="auth_api_login"),
]

urlpatterns = [
    path("api/", include(api_router)),
]
