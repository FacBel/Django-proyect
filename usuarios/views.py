from django.shortcuts import render, redirect
from .forms import UsuarioPersonalizadoForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UsuarioPersonalizadoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("menu")
    else:
        form = UsuarioPersonalizadoForm()
    return render(request, "registration/register.html", {"form":form})