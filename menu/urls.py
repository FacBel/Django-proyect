from django.urls import path
from . import views 

urlpatterns = [
    path('', views.menu, name="menu"),
    path('nueva/', views.crear_pizza, name="crear_pizza"),
    path("editar/<int:id>/", views.editar_pizza, name="editar_pizza"),
    path("borrar/<int:id>", views.eliminar_pizza, name="eliminar_pizza"),
    path("register/", views.register, name="register"),
]

