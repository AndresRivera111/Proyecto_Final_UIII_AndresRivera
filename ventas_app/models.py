from django.db import models

# Create your models here.
class Ventas(models.Model):
    id_ventas = models.IntegerField()
    id_empleado = models.IntegerField()
    id_cliente = models.IntegerField()
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()
    fecha_venta = models.DateTimeField()
    total = models.IntegerField()