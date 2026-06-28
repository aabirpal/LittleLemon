from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


def index(request):
    return render(request, "index.html")


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Alias for compatibility with variations of instructions/tests
MenuItemView = MenuItemsView