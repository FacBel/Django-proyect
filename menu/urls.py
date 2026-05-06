from django.urls import path
from . import views 

urlpatterns = [
    path('', views.menu, name="menu"),
    path('nueva/', views.crear_categoria, name="crear_categoria"),
]


