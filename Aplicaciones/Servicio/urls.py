from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home),
    path('registrarTrabajo/', views.registrarTrabajo),
    path('edicionTrabajo/<codigo>', views.edicionTrabajo),
    path('editarTrabajo/', views.editarTrabajo),
    path('eliminarTrabajo/<codigo>', views.eliminarTrabajo),
    path('salir/', views.salir, name="salir")
]