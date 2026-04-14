from django.shortcuts import render

def inicio(request):
    return render(request, "bienvenida/index.html", name= "home")