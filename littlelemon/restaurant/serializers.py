from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Menu
        fields = ['title', 'price', 'inventory', 'category_id']