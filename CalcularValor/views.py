from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'home.html', {"listaTiposMadera" : listaTiposMadera })

def calcularValorPieza(request):
    piezaMadera = PiezaMadera()
    tipoMadera = TipoMadera.objects.get(idTipoMadera=request.POST['tipoMadera'])
    piezaMadera.tipoMadera = tipoMadera
    piezaMadera.alto = request.POST['txtAlto']
    piezaMadera.ancho = request.POST['txtAncho']
    piezaMadera.largo = request.POST['txtLargo']
    tipoMadera = TipoMadera.objects.get(idTipoMadera = request.POST['tipoMadera'])
    piezaMadera.valorPieza = piezaMadera.totalValorPieza(tipoMadera.valorPie)
    print(piezaMadera.valorPieza)
    return render(request, 'detallesPiezaMadera.html', {"piezaMadera" : piezaMadera })

def detallesPiezaMadera(request, piezaMadera):
    return render('detallesPiezaMadera.html', {"piezaMadera": piezaMadera})

def tiposMadera(request):
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'tiposMadera.html')
