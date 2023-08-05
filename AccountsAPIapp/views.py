from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate, get_user_model
from AccountsAPIapp.authentication import EmailAuthenticationBackend
from .models import AccountsAPICustomUser
from .serializer import AccountsAPICustomUserSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = AccountsAPICustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email, password)
        user = AccountsAPICustomUser.objects.get(email=email)
        print(user.email, user.password)
        login_instance = EmailAuthenticationBackend()
        user = login_instance.authenticate(email=email, password=password)
        print(user)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.any}, status=status.HTTP_200_OK)
        return Response({'erroe': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)