from django.db import models
from app.models import Menu
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField() 
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits = 6, decimal_places=2) 
    
    class Meta:
        unique_together =  ("menu_item","user")
    

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="DeliveryCrew",null=True) 
    status = models.BooleanField(db_index=True,default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2) 
    date = models.DateField(db_index=True) 

class OrderItem(models.Model):
    order = models.ForeignKey(User,on_delete=models.CASCADE) 
    menu_item = models.ForeignKey(Menu,on_delete=models.CASCADE) 
    quantity = models.SmallIntegerField() 
    unit_price = models.DecimalField(max_digits=6,decimal_places=2) 
    price = models.DecimalField(max_digits=6, decimal_places=2) 
    
    class Meta:
        unique_together = ("order","menu_item")  