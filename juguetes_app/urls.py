from django.urls import path
from juguetes_app import views

urlpatterns = [
    #inicio jugueteria
    path('juguetes', views.inicio_vistaJuguetes, name='juguetes'),
    path('registrarJuguetes/', views.registrarJuguetes, name='registrarJuguetes'),
    path('seleccionarJuguetes/<id>', views.seleccionarJuguetes, name='seleccionarJuguetes'),
    path('editarJuguetes/', views.editarJuguetes, name='editarJuguetes'),
    path('borrarJuguetes/<id>', views.borrarJuguetes, name='borrarJuguetes' ),
]
