from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','full_name','email','is_active','is_admin')


class UserCreationSerialier(serializers.Serializer):
    full_name = serializers.CharField(max_length=80)
    email = serializers.EmailField(max_length=120)
    password = serializers.CharField()
    
class UserEditionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('full_name','email')
