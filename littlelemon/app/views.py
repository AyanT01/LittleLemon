from django.shortcuts import render
from .forms import Booking_Form
from .models import Menu
# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def book(request):
    form = Booking_Form() 
    if request.method == "POST":
        form = Booking_Form(request.POST) 
        if form.is_valid():
            form.save() 
    context = {"form":form}
    return render(request,"booking.html",context) 

def menu(request):
    menu_items = Menu.objects.all() 
    menu_items_dict = {"menu_items":menu_items}
    return render(request,"menu.html",menu_items_dict)

def display_menu_items(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(id=pk) 
    else:
        menu_item = ""
    menu_item_dict = {
        "menu_item":menu_item
    }
    return render(request,"menu_item.html",menu_item_dict)