from django.shortcuts import render, redirect
from .models import Proveedores

# Create your views here.
def inicio_vistaProveedores (request):
    proveedores = Proveedores.objects.all()
    return render(request, 'gestionarProveedores.html', {'misProveedores' : proveedores})

def registrarProveedores(request):
    id_proveedor=request.POST['txtid_proveedor']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txttelefono']
    correo_electronico=request.POST['txtcorreo_electronico']
    vehiculo=request.POST['txtvehiculo']
    horario=request.POST['txthorario']

    guardarProveedor=Proveedores.objects.create(
    id_proveedor=id_proveedor, nombre=nombre, direccion=direccion, telefono=telefono, correo_electronico=correo_electronico, vehiculo=vehiculo, horario=horario)
    return redirect("proveedores")

def seleccionarProveedores(request, id_proveedor):
    proveedores = Proveedores.objects.get(id_proveedor=id_proveedor)
    return render(request,'editarProveedores.html', {'misProveedores': proveedores})

def editarProveedores(request):
    id_proveedor=request.POST['txtid_proveedor']
    nombre=request.POST['txtnombre']
    direccion=request.POST['txtdireccion']
    telefono=request.POST['txttelefono']
    correo_electronico=request.POST['txtcorreo_electronico']
    vehiculo=request.POST['txtvehiculo']
    horario=request.POST['txthorario']
    proveedores = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedores.id_proveedor=id_proveedor
    proveedores.nombre = nombre
    proveedores.direccion = direccion
    proveedores.telefono = telefono
    proveedores.correo_electronico = correo_electronico
    proveedores.vehiculo = vehiculo
    proveedores.horario = horario
    proveedores.save() # guarda registro actualizado
    return redirect("proveedores")

def borrarProveedores(request, id_proveedor):
    proveedores = Proveedores.objects.get(id_proveedor=id_proveedor)
    proveedores.delete() # borra el registro
    return redirect("proveedores")