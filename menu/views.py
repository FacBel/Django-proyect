from django.shortcuts import render, redirect
from .models import Pizza
from .forms import CategoriaForm

def menu(request):
    pizzas = Pizza.objects.all()

    return render(request, "menu/index.html", {
        "pizzas": pizzas
    })

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("menu")
    else:
        form = CategoriaForm()
    return render(request, "menu/crear_categoria.html", {"form":form})