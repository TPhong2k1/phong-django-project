from django.urls import path
from .views import admin_home, register_view, list_view

urlpatterns = [
    path('', admin_home, name='admin_home'), #Trang quản trị chính
    path('', register_view, name='register'),
    path('danhsach/', list_view, name='list'),
]