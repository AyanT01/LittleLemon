from django.urls import path,include 
from . import views 
urlpatterns = [
    path("api/menu-items", views.MenuItemView.as_view()),
    path("api/menu-items1", views.menu_items),
    path("api/single-menuitem/<int:pk>",views.single_menu_item),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("managers",views.managers),
    path("api/groups/delivery-crew/users/<int:pk>",views.delivery_crew),
    path("api/orders",views.orders),
]