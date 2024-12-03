from django.shortcuts import render, redirect
from .models import Sucursales

# Create your views here.
def inicio_vistaSucursales (request):
    sucursales = Sucursales.objects.all()
    return render(request, 'gestionarSucursales.html', {'misSucursales' : sucursales})

def registrarSucursales(request):
    id_sucursal=request.POST['txtid_sucursal']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txttelefono']
    horario=request.POST['txthorario']
    correo_electronico=request.POST['txtcorreo_electronico']
    codigo_postal=request.POST['txtcodigo_postal']

    guardarSucursal=Sucursales.objects.create(
    id_sucursal=id_sucursal, nombre=nombre, direccion=direccion, telefono=telefono, horario=horario, correo_electronico=correo_electronico, codigo_postal=codigo_postal)
    return redirect("sucursales")

def seleccionarSucursales(request, id_sucursal):
    sucursales = Sucursales.objects.get(id_sucursal=id_sucursal)
    return render(request,'editarSucursales.html', {'misSucursales': sucursales})

def editarSucursales(request):
    id_sucursal=request.POST['txtid_sucursal']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txttelefono']
    horario=request.POST['txthorario']
    correo_electronico=request.POST['txtcorreo_electronico']
    codigo_postal=request.POST['txtcodigo_postal']
    sucursales = Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursales.id_sucursal = id_sucursal
    sucursales.nombre = nombre
    sucursales.direccion = direccion
    sucursales.telefono = telefono
    sucursales.horario = horario
    sucursales.correo_electronico = correo_electronico
    sucursales.codigo_postal = codigo_postal
    sucursales.save() # guarda registro actualizado
    return redirect("sucursales")

def borrarSucursales(request, id_sucursal):
    sucursales = Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursales.delete() # borra el registro
    return redirect("sucursales")