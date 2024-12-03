from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_clientes = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    correo_electronico = models.CharField(max_length=20)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=40)
    forma_pago = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre