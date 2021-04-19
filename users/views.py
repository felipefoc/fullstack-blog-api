from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.decorators import api_view, permission_classes
from .serializers import UsersSerializer, AdminSeriealizers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def test(request):
    """
    alaal
    """
    return Response({"message": "Hello, world!"})



