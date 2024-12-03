from django.urls import path
from sucursales_app import views

urlpatterns = [
    #inicio jugueteria
    path('sucursales', views.inicio_vistaSucursales, name='sucursales'),
    path('registrarSucursales/', views.registrarSucursales, name='registrarSucursales'),
    path('seleccionarSucursales/<id_sucursal>', views.seleccionarSucursales, name='seleccionarSucursales'),
    path('editarSucursales/', views.editarSucursales, name='editarSucursales'),
    path('borrarSucursales/<id_sucursal>', views.borrarSucursales, name='borrarSucursales' ),
]
