from django.db import models

# Create your models here.
class Marcas(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    sucursal = models.CharField(max_length=20)
    correo_electronico = models.CharField(max_length=40)
    telefono = models.IntegerField()
    distribuidores = models.CharField(max_length=40)
    tipo_producto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre