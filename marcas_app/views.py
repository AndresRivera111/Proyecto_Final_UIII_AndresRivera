from django.shortcuts import render, redirect
from .models import Marcas

# Create your views here.
def inicio_vistaMarcas (request):
    marcas = Marcas.objects.all()
    return render(request, 'gestionarMarcas.html', {'misMarcas' : marcas})

def registrarMarcas(request):
    id_marca=request.POST['txtid_marca']
    nombre=request.POST['txtnombre']
    sucursal=request.POST['txtsucursal']
    correo_electronico=request.POST['txtcorreo_electronico']
    telefono=request.POST['txttelefono']
    distribuidores=request.POST['txtdistribuidores']
    tipo_producto=request.POST['txttipo_producto']

    guardarMarcas=Marcas.objects.create(
    id_marca=id_marca, nombre=nombre, sucursal=sucursal, correo_electronico=correo_electronico, telefono=telefono, distribuidores=distribuidores, tipo_producto=tipo_producto)
    return redirect("marcas")

def seleccionarMarcas(request, id_marca):
    marcas = Marcas.objects.get(id_marca=id_marca)
    return render(request,'editarMarcas.html', {'misMarcas': marcas})

def editarMarcas(request):
    id_marca=request.POST['txtid_marca']
    nombre=request.POST['txtnombre']
    sucursal=request.POST['txtsucursal']
    correo_electronico=request.POST['txtcorreo_electronico']
    telefono=request.POST['txttelefono']
    distribuidores=request.POST['txtdistribuidores']
    tipo_producto=request.POST['txttipo_producto']
    marcas = Marcas.objects.get(id_marca=id_marca)
    marcas.id_marca = id_marca
    marcas.nombre = nombre
    marcas.sucursal = sucursal
    marcas.correo_electronico = correo_electronico
    marcas.telefono = telefono
    marcas.distribuidores = distribuidores
    marcas.tipo_producto = tipo_producto
    marcas.save() # guarda registro actualizado
    return redirect("marcas")

def borrarMarcas(request, id_marca):
    marcas = Marcas.objects.get(id_marca=id_marca)
    marcas.delete() # borra el registro
    return redirect("marcas")