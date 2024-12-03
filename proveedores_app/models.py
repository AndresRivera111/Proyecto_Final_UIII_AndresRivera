from django.db import models

# Create your models here.
class Proveedores(models.Model):
    id_proveedor = models.CharField(primary_key=True, max_length=11)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.CharField(max_length=40)
    vehiculo = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre