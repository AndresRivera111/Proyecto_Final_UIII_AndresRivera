from django.shortcuts import render, redirect
from .models import Juguetes

# Create your views here.
def inicio_vistaJuguetes (request):
    juguetes = Juguetes.objects.all()
    return render(request, 'gestionarJuguetes.html', {'misJuguetes' : juguetes})

def registrarJuguetes(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    marca=request.POST['txtmarca']
    fecha_fabricacion=request.POST['txtfecha_fabricacion']
    precio=request.POST['numbprecio']
    proveedor=request.POST['txtproveedor']
    clasificacion=request.POST['txtclasificacion']

    guardarJuguetes=Juguetes.objects.create(
    id=id, nombre=nombre, marca=marca, fecha_fabricacion=fecha_fabricacion, precio=precio, proveedor=proveedor, clasificacion=clasificacion)
    return redirect("juguetes")

def seleccionarJuguetes(request, id):
    juguetes = Juguetes.objects.get(id=id)
    return render(request,'editarJuguetes.html', {'misJuguetes': juguetes})

def editarJuguetes(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    marca=request.POST['txtmarca']
    fecha_fabricacion=request.POST['txtfecha_fabricacion']
    precio = request.POST['numbprecio']
    proveedor = request.POST['txtproveedor']
    clasificacion = request.POST['txtclasificacion']
    juguete = Juguetes.objects.get(id=id)
    juguete.id = id
    juguete.nombre = nombre
    juguete.marca = marca
    juguete.fecha_fabricacion = fecha_fabricacion
    juguete.precio = precio
    juguete.proveedor = proveedor
    juguete.clasificacion = clasificacion
    juguete.save() # guarda registro actualizado
    return redirect("juguetes")

def borrarJuguetes(request, id):
    juguete = Juguetes.objects.get(id=id)
    juguete.delete() # borra el registro
    return redirect("juguetes")