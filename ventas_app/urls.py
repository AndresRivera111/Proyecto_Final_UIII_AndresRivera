from django.urls import path
from ventas_app import views

urlpatterns = [
    #inicio jugueteria
    path('ventas', views.inicio_vistaVentas, name='ventas'),
    path('registrarVentas/', views.registrarVentas, name='registrarVentas'),
    path('seleccionarVentas/<id_ventas>', views.seleccionarVentas, name='seleccionarVentas'),
    path('editarVentas/', views.editarVentas, name='editarVentas'),
    path('borrarVentas/<id_ventas>', views.borrarVentas, name='borrarVentas' ),
]
