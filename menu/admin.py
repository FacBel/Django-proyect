from django.contrib import admin
from .models import Pizza, Categoria

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "Categoria")
    list_filter = ("Categoria",)
    search_fields = ("nombre",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
