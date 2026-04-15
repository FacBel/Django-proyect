from django.shortcuts import render
from .models import Pizza

def menu(request):
    pizzas = Pizza.objects.all()

    return render(request, "menu/index.html", {
        "pizzas": pizzas
    })