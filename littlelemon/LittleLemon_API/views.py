from django.shortcuts import render
from rest_framework.response import Response 
from app.models import Menu
from .serializers import MenuItemSerializer
from rest_framework import generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model 
from . serializers import UserSerializer


@api_view(["GET","POST","PUT","PATCH","DELETE"]) 
#@permission_classes([IsAuthenticated])
def menu_items(request):
    if request.method == "GET":
        paginator = PageNumberPagination() 
        paginator.page_size = 2 
        items = Menu.objects.all() 
        result_page = paginator.paginate_queryset(items,request)
        serialized_items = MenuItemSerializer(result_page,many=True)
        return paginator.get_paginated_response(serialized_items.data)
        #return Response(serialized_items.data,status=200)
    if request.method == "POST":
        if request.user.groups.filter(name="Manager").exists():
            serialized_item = MenuItemSerializer(data=request.data)
            serialized_item.is_valid(raise_exception=True)
            serialized_item.save() 
            return Response(serialized_item.data,status=201)
        return Response({"message":"You are not authorized."})
    """if request.method == "PUT":
        try:
            pk = request.data.get(id)
            item = Menu.objects.get(pk)
            return Response({"message":"Operation Successful"})
        except Menu.DoesNotExist:
            return Response({"message":"item not found"})
    if request.method == "PATCH":
        pass """

@api_view(["GET","POST","PUT","PATCH","DELETE"]) 
@permission_classes([IsAuthenticated])
def managers(request):
    if request.method == "GET":
        UserModel = get_user_model().objects
        serialized_item = UserSerializer(UserModel,many=True) 
        return Response(serialized_item.data)
        
@api_view()
def single_menu_item(request,pk):
    if request.method == "GET":
        item = get_object_or_404(Menu,id=pk)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)    
        

class MenuItemView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
