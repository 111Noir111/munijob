from django.shortcuts import render, redirect
from .models import Trabajo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


@login_required
def home(request):
    listaTrabajos = Trabajo.objects.all()
    messages.success(request, '¡Trabajos listados!')
    return render(request, "gestionServicios.html", {"trabajos": listaTrabajos})

def registrarTrabajo(request):
    codigo = request.POST['txtCodigo']
    nombreTrabajo = request.POST['txtNombreTrabajo']
    descripcion = request.POST['txtDescripcion']
    
    trabajo = Trabajo.objects.create(
        codigo=codigo, nombreTrabajo=nombreTrabajo, descripcion=descripcion)
    messages.success(request, '¡Trabajo registrado!')
    return redirect('/')

def edicionTrabajo(request, codigo):
    trabajo = Trabajo.objects.get(codigo=codigo)
    return render(request, "edicionTrabajo.html", {"trabajo":trabajo})

def editarTrabajo(request):
    codigo = request.POST['txtCodigo']
    nombreTrabajo = request.POST['txtNombreTrabajo']
    descripcion = request.POST['txtDescripcion']
    
    trabajo = Trabajo.objects.get(codigo=codigo)
    trabajo.nombreTrabajo = nombreTrabajo
    trabajo.descripcion = descripcion
    trabajo.save()
    messages.success(request, '¡Trabajo actualizado!')
    return redirect('/')

def eliminarTrabajo(request, codigo):
    trabajo = Trabajo.objects.get(codigo=codigo)
    trabajo.delete()
    messages.success(request, '¡Trabajo eliminado!')
    return redirect('/')

def salir(request):
    logout(request)
    return redirect('/')