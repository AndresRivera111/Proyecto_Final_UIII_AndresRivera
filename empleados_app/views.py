from django.shortcuts import render, redirect
from .models import Empleados

# Create your views here.
def inicio_vistaEmpleados (request):
    empleados = Empleados.objects.all()
    return render(request, 'gestionarEmpleados.html', {'misEmpleados' : empleados})

def registrarEmpleados(request):
    id_empleado=request.POST['txtid_empleado']
    nombre=request.POST['txtnombre']
    edad=request.POST['txtedad']
    rfc=request.POST['txtrfc']
    curp=request.POST['txtcurp']
    correo_electronico=request.POST['txtcorreo_electronico']
    telefono=request.POST['txttelefono']

    guardarEmpleado=Empleados.objects.create(
    id_empleado=id_empleado, nombre=nombre, edad=edad, rfc=rfc, curp=curp, correo_electronico=correo_electronico, telefono=telefono)
    return redirect("empleados")

def seleccionarEmpleados(request, id_empleado):
    empleado = Empleados.objects.get(id_empleado=id_empleado)
    return render(request,'editarEmpleados.html', {'misEmpleados': empleado})

def editarEmpleados(request):
    id_empleado=request.POST['txtid_empleado']
    nombre=request.POST['txtnombre']
    edad=request.POST['txtedad']
    rfc=request.POST['txtrfc']
    curp=request.POST['txtcurp']
    correo_electronico=request.POST['txtcorreo_electronico']
    telefono=request.POST['txttelefono']
    empleados = Empleados.objects.get(id_empleado=id_empleado)
    empleados.id_empleado = id_empleado
    empleados.nombre = nombre
    empleados.edad = edad
    empleados.rfc = rfc
    empleados.curp = curp
    empleados.correo_electronico = correo_electronico
    empleados.telefono = telefono
    empleados.save() # guarda registro actualizado
    return redirect("empleados")

def borrarEmpleados(request, id_empleado):
    empleados = Empleados.objects.get(id_empleado=id_empleado)
    empleados.delete() # borra el registro
    return redirect("empleados")