# Generated by Django 5.1.3 on 2024-12-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id_proveedor', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=20)),
                ('correo_electronico', models.CharField(max_length=40)),
                ('vehiculo', models.CharField(max_length=20)),
                ('horario', models.CharField(max_length=20)),
            ],
        ),
    ]
