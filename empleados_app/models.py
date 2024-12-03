from django.db import models

# Create your models here.
class Empleados(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    rfc = models.CharField(max_length=40)
    curp = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=20)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre