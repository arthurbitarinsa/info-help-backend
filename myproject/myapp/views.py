# myapp/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            return Response({"detail": "Successfully logged in."}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
