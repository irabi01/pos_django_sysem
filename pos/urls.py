from django.urls import path, include
from . import views



urlpatterns = [
    path('', views._loginView, name = "_loginView"),
    path('pos/dashboard/', views._dashboard, name = "_dashboard"),
    path('pos/dashboard/inventory/', views._inventory, name = "_inventory")
]