from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza
from .forms import PizzaForm
from django.contrib.auth.decorators import login_required



def menu(request):
    pizzas = Pizza.objects.all()

    return render(request, "menu/index.html", {
        "pizzas": pizzas
    })

@login_required
def crear_pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("menu")
    else:
        form = PizzaForm()
    return render(request, "menu/crear_pizza.html", {"form":form})

@login_required
def editar_pizza(request, id):

    pizza = get_object_or_404(Pizza, id=id)

    if request.method == "POST":
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect("menu")
    else:
        form = PizzaForm(instance=pizza)
    return render(request, "menu/editar_pizza.html", {"form":form})

@login_required
def eliminar_pizza(request, id):

    pizza = get_object_or_404(Pizza, id=id)

    if request.method == "POST":
        pizza.delete() # Podria ser borrado logico.
        return redirect("menu")
    
    return render(request, "menu/borrar_pizza.html", {"pizza":pizza})