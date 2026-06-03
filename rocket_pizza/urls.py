
from django.contrib import admin
from django.urls import path, include
from usuarios.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bienvenida.urls')),
    path('menu/', include('menu.urls')),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('cuentas/register/', register, name="register"),
]
