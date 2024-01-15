from django.shortcuts import render
from rest_framework.response import Response 
from app.models import Menu
from .serializers import MenuItemSerializer
from rest_framework import generics
class MenuItemView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
