from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers.auth import AuthTokenObtainPairSerializer


class AuthTokenObtainPairView(TokenObtainPairView):
    serializer_class = AuthTokenObtainPairSerializer