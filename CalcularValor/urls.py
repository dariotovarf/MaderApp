from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('detallesPiezaMadera/', views.detallesPiezaMadera),
    path('calcularValorPieza/', views.calcularValorPieza, name='calcularValorPieza'),
    path('tiposMadera/', views.tiposMadera, name='tiposMadera'),
    path('registrarTipoMadera/', views.registrarTipoMadera, name='registrarTipoMadera'),
    path('registrarLote/', views.registrarLote, name='registrarLote'),
    path('listarLotesMadera', views.listarLotesMadera, name= 'listarLotesMadera'),
    path('listarLotesMaderaDetalles/<idLote>', views.listarLotesMaderaDetalles, name= 'listarLotesMaderaDetalles'),
    path('eliminarPiezaMadera/<idPieza>', views.eliminarPiezaMadera, name='eliminarPiezaMadera'),
    path('edicionTipoMadera/<idTipoMadera>', views.edicionTipoMadera, name='edicionTipoMadera'),
    path('editarTipoMadera/', views.editarTipoMadera, name='editarTipoMadera'),
    
]
