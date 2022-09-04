from rest_framework import generics,viewsets
from users.models import User
from api.serializers.users import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer