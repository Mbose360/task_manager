from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

class Registerview(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class = UserSerializer

