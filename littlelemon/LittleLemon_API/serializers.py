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
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["user","menu_item","quantity","unit_price","price"]#,"user","quantity"]
        model = Cart
"""class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField() 
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits = 6, decimal_places=2) 
    
    class Meta:
        unique_together =  ("menu_item","user")"""