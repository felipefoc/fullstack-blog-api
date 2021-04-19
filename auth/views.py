from .serializers import UsersSerializer
from rest_framework import generics, status, serializers, permissions,viewsets
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema




class RegisterView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = UsersSerializer
    queryset = User.objects.all()