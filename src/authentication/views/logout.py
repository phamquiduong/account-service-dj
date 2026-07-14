from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenBlacklistView


@extend_schema(tags=["Authentication"])
class LogoutAPIView(TokenBlacklistView):
    pass
