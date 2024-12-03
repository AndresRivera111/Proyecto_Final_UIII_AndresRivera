from django.db import models

# Create your models here.
class Sucursales(models.Model):
    id_sucursal = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    horario = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=20)
    codigo_postal = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre