from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializer
from django.contrib.auth.models import User

# Function Based Views
@api_view(['GET', 'POST', 'DELETE', 'GET',  'PUT'])
def function_based_view(request, *args, **kwargs):
    if request.method == 'GET':
        """
        Lista usuários
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        """
        Deletar usuário
        """
        try:
            user = User.objects.get(pk=kwargs["id"]).delete()
            return Response({"Success": "User deleted"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"Error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        """
        Editar usuário
        """
        try:
            user = User.objects.get(pk=kargs["id"])
            return Response({'ok':'ok'})
        except:
            return Response({"erro":"erro"})

    elif request.method == 'POST':
        """
        Criar usuário
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_406_NOT_ACCEPTABLE)



