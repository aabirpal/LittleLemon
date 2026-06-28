from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']

# Alias for compatibility with variations of instructions/tests
MenuItemSerializer = MenuSerializer
