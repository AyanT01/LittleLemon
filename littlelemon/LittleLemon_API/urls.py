from django.urls import path,include 
from . import views 
urlpatterns = [
    path("api/menu-items", views.MenuItemView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]