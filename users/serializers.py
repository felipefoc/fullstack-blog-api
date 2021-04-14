from rest_framework import serializers
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'is_superuser']

class AdminSeriealizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
