from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated



class ListAndCreate(generics.ListCreateAPIView):
    """
    Lista e cria usuários
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retorna, atualiza e delete um usuário
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    