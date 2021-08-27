from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (RegistrationSerializer, ActivationSerializer,
                          ChangePasswordSerializer, ForgotPasswordSerializer, LoginSerializer)
from rest_framework.authtoken.views import ObtainAuthToken

class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
            return Response('Account created succesfully', status=201)

class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Account activated', status=status.HTTP_200_OK)

class LoginView(ObtainAuthToken):
    pass

class LogoutView():
    pass

class ChangePasswordView():
    pass

class ForgotPasswordView():
    pass