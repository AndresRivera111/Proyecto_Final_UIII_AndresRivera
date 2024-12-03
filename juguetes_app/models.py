from django.db import models

# Create your models here.
class Juguetes(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=40)
    fecha_fabricacion = models.DateField()
    marca = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.CharField(max_length=20)
    clasificacion = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
