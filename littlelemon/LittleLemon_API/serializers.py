from rest_framework import serializers
from app.models import Menu

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = ["id","name","price","description"]