from django.urls import path
from marcas_app import views

urlpatterns = [
    #inicio jugueteria
    path('marcas', views.inicio_vistaMarcas, name='marcas'),
    path('registrarMarcas/', views.registrarMarcas, name='registrarMarcas'),
    path('seleccionarMarcas/<id_marca>', views.seleccionarMarcas, name='seleccionarMarcas'),
    path('editarMarcas/', views.editarMarcas, name='editarMarcas'),
    path('borrarMarcas/<id_marca>', views.borrarMarcas, name='borrarMarcas'),
]
