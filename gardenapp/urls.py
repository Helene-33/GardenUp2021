from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index, name='index'),
    path('plants/', views.plants, name='plants'),
    path('plantDetail/<int:id>', views.plantDetail, name='detail'),
    path('newplant/', views.newPlant, name='newplant'),
]