from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('zapatillas/zapatillas_basquetball/', views.zapatillas_basquetball, name='zapatillas_basquetball'),

    path('agregar_zapatillas', views.agregar_producto, name='agregar_zapatillas'),

    path('listar_zapatillas', views.listar_producto, name='listar_zapatillas'),

    path('editar_zapatillas/<id>', views.editar_producto, name='editar_zapatillas'),

    path('eliminar_zapatillas/<id>', views.eliminar_producto, name='eliminar_zapatillas'),
    
]