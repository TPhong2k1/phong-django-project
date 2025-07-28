from django.urls import path
from .views import register_view, list_view

urlpatterns = [
    path('', register_view, name='register'),
    path('danhsach/', list_view, name='list'),
]