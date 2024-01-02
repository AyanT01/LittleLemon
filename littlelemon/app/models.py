from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50) 
    price = models.IntegerField() 
    description = models.CharField(max_length=1000,default="African Dish")

    def __str__(self):
        return f"{self.name}"

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    phone_number = models.IntegerField() 
    comment = models.CharField(max_length=1000) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"