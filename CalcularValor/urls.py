from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('detallesPiezaMadera/', views.detallesPiezaMadera),
    path('calcularValorPieza/', views.calcularValorPieza),
    path('tiposMadera/', views.tiposMadera),
]
