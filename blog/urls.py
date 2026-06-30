# blog/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('home/', views.home_page, name='home'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
    path('libro/<int:libro_id>/', views.perfil_libro, name='perfil_libro'),

    # ✅ NUEVO: leer capítulo (lector con scroll infinito)
    path('libro/<int:libro_id>/leer/', views.leer_capitulo, name='leer_capitulo'),

    path('escribir/', views.subir_libro, name='subir_libro'),
    path('escribir/guardar/', views.guardar_libro, name='guardar_libro'),
    path('admin-panel/', views.panel_administrador, name='panel_administrador'),
    path('registro/', views.registro, name='registro'),
    # ✅ eliminar libro
    path('libro/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)