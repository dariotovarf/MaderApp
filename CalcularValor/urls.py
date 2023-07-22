from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('detallesPiezaMadera/', views.detallesPiezaMadera),
    path('calcularValorPieza/', views.calcularValorPieza, name='calcularValorPieza'),
    path('tiposMadera/', views.tiposMadera, name='tiposMadera'),
    path('registrarTipoMadera/', views.registrarTipoMadera, name='registrarTipoMadera')
]
