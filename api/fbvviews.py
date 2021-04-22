from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializer
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User

# Function Based Views
@api_view(['GET', 'POST', 'DELETE', 'GET',  'PATCH'])
def function_based_view(request, *args, **kwargs):
    users = User.objects.all()

    if request.method == 'GET' and not kwargs:
        """
        Lista usuários
        """
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'GET' and kwargs:
        """
        Lista usuários
        """
        user = get_object_or_404(users, pk=kwargs["pk"])
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        """
        Deletar usuário
        """
        user = get_object_or_404(users, pk=kwargs["pk"])
        user.delete()
        return Response({"Success": "User has been deleted"}, status=status.HTTP_206_PARTIAL_CONTENT)

    elif request.method == 'PATCH':
        """
        Editar usuário
        """
        user = get_object_or_404(users, pk=kwargs["pk"])
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'POST':
        """
        Criar usuário
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




