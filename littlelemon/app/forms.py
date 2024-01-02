from django.forms import ModelForm 
from .models import Booking

class Booking_Form(ModelForm):
    class Meta:
        fields = "__all__"
        model = Booking 