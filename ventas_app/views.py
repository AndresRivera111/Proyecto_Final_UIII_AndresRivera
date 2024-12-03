from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.
def inicio_vistaVentas (request):
    ventas = Ventas.objects.all()
    return render(request, 'gestionarVentas.html', {'misVentas' : ventas})

def registrarVentas(request):
    id_ventas=request.POST['txtid_ventas']
    id_empleado=request.POST['txtid_empleado']
    id_cliente=request.POST['txtid_cliente']
    id_producto=request.POST['txtid_producto']
    cantidad=request.POST['txtcantidad']
    fecha_venta=request.POST['txtfecha_venta']
    total=request.POST['txttotal']

    guardarVenta=Ventas.objects.create(
    id_ventas=id_ventas, id_empleado=id_empleado, id_cliente=id_cliente, id_producto=id_producto, cantidad=cantidad, fecha_venta=fecha_venta, total=total)
    return redirect("ventas")

def seleccionarVentas(request, id_ventas):
    ventas = Ventas.objects.get(id_ventas=id_ventas)
    return render(request,'editarVentas.html', {'misVentas': ventas})

def editarVentas(request):
    id_ventas=request.POST['txtid_ventas']
    id_empleado=request.POST['txtid_empleado']
    id_cliente=request.POST['txtid_cliente']
    id_producto=request.POST['txtid_producto']
    cantidad=request.POST['txtcantidad']
    fecha_venta=request.POST['txtfecha_venta']
    total=request.POST['txttotal']
    ventas = Ventas.objects.get(id_ventas=id_ventas)
    ventas.id_ventas = id_ventas
    ventas.id_empleado = id_empleado
    ventas.id_cliente = id_cliente
    ventas.id_producto = id_producto
    ventas.cantidad = cantidad
    ventas.fecha_venta = fecha_venta
    ventas.total = total
    ventas.save() # guarda registro actualizado
    return redirect("ventas")

def borrarVentas(request, id_ventas):
    ventas = Ventas.objects.get(id_ventas=id_ventas)
    ventas.delete() # borra el registro
    return redirect("ventas")