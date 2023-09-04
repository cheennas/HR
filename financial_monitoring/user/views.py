from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer
from general_info.models import GeneralInfo


class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

