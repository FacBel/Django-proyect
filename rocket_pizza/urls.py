
from django.contrib import admin
from django.urls import path, include
from usuarios.views import register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bienvenida.urls')),
    path('menu/', include('menu.urls')),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('cuentas/register/', register, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)