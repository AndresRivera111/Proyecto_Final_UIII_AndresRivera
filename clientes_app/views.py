from django.shortcuts import render, redirect
from .models import Clientes

# Create your views here.
def inicio_vistaClientes (request):
    clientes = Clientes.objects.all()
    return render(request, 'gestionarClientes.html', {'misClientes' : clientes})

def registrarClientes(request):
    id_clientes=request.POST['txtid_clientes']
    nombre=request.POST['txtnombre']
    edad=request.POST['txtedad']
    correo_electronico=request.POST['txtcorreo_electronico']
    telefono=request.POST['txttelefono']
    direccion=request.POST['txtdireccion']
    forma_pago=request.POST['txtforma_pago']

    guardarCliente=Clientes.objects.create(
    id_clientes=id_clientes, nombre=nombre, edad=edad, correo_electronico=correo_electronico, telefono=telefono, direccion=direccion, forma_pago=forma_pago)
    return redirect("clientes")

def seleccionarClientes(request, id_clientes):
    cliente = Clientes.objects.get(id_clientes=id_clientes)
    return render(request,'editarClientes.html', {'misClientes': cliente})

def editarClientes(request):
    id_clientes=request.POST['txtid_clientes']
    nombre=request.POST['txtnombre']
    edad=request.POST['txtedad']
    correo_electronico=request.POST['txtcorreo_electronico']
    telefono=request.POST['txttelefono']
    direccion=request.POST['txtdireccion']
    forma_pago=request.POST['txtforma_pago']
    clientes = Clientes.objects.get(id_clientes=id_clientes)
    clientes.id_clientes = id_clientes
    clientes.nombre = nombre
    clientes.edad = edad
    clientes.correo_electronico = correo_electronico
    clientes.telefono = telefono
    clientes.direccion = direccion
    clientes.forma_pago = forma_pago
    clientes.save() # guarda registro actualizado
    return redirect("clientes")

def borrarClientes(request, id_clientes):
    clientes = Clientes.objects.get(id_clientes=id_clientes)
    clientes.delete() # borra el registro
    return redirect("clientes")