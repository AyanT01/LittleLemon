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
    if request.user.groups.filter(name="Manager").exists():
        UserModel = get_user_model().objects.all()
        Manager = get_user_model().objects.filter(groups__name='Manager')
        if request.method == "GET":
            serialized_item = UserSerializer(UserModel,many=True) 
            return Response(serialized_item.data)
        username = request.data["username"]
        if username:
            user = get_object_or_404(UserModel, username=username)
            #managers = UserModel.objects.get(name='Manager')
            if request.method == 'POST':
                Manager.user_set.add(user)
            elif request.method == 'DELETE':
                Manager.user_set.remove(user)
            return Response({"message": 'ok'})
    else:
        return Response({'message': 'error'})
        
        
@api_view(["GET","POST","PUT","PATCH","DELETE"])
def single_menu_item(request,pk):
    if request.method == "GET":
        item = get_object_or_404(Menu,id=pk)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)    
    if request.user.groups.filter(name="Manager").exists():
        if request.method == "POST":
            serialized_item = MenuItemSerializer(data=request.data)
            serialized_item.is_valid(raise_exception=True) 
            serialized_item.save() 
            return Response(serialized_item.data) 
            pass 
        if request.method == "DELETE":
            Menu.objects.filter(id=pk).delete()
            return Response({"message":"Deletion successful"})
        if request.method == "PUT":
            item = Menu.objects.get(pk=pk)
            item_data = MenuItemSerializer(instance=item, data=request.data)
            item_data.is_valid(raise_exception=True) 
            item_data.save() 
            return Response(item_data.data)
        if request.method == "PATCH":
            item = Menu.objects.get(id=pk) 
            item_data = MenuItemSerializer(instance=item,data=request.data,partial=True)
            item_data.is_valid(raise_exception=True) 
            item_data.save() 
            return Response(item_data.data)
            pass
    else:
        return Response({"message":"You are not authorized"})

class MenuItemView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

"""

        if request.method == "POST":
            serialized_item = UserSerializer(data=request.data)
            serialized_item.is_valid(raise_exception=True) 
            serialized_item.save() 
            return Response(serialized_item.data) 
            pass
    
    else:
        return Response({"message":"You are not authorized"})

"""