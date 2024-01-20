from rest_framework import serializers
from app.models import Menu
from django.contrib.auth import get_user_model 
from . models import Order, OrderItem, Cart
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = ["id","name","price","description"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user","status","total","date"]