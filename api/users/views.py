# rest framework
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

# current app
from .serializers import RegisterSerializer, LoginSerializer, UsersSerializer
from .models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UsersSerializer
    lookup_field = "id"
