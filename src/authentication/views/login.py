from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView


@extend_schema(tags=["Authentication"])
class LoginAPIView(TokenObtainPairView):
    pass
