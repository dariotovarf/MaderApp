from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

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
    listaPiezas = []
    listaPiezas.append(piezaMadera)
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'home.html', {"listaPiezas" : listaPiezas, "listaTiposMadera" : listaTiposMadera })

def detallesPiezaMadera(request, piezaMadera):
    return render('detallesPiezaMadera.html', {"piezaMadera": piezaMadera})

def tiposMadera(request):
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'tiposMadera.html', {'listaTiposMadera': listaTiposMadera})

def registrarTipoMadera(request):
    nombre = request.POST['txtNombre']
    valorPie = request.POST['txtValor']
   

    tipoMadera = TipoMadera.objects.create(nombre=nombre, valorPie=valorPie)
    messages.success(request, 'Tipo de Madera Registrada')
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'tiposMadera.html', {'listaTiposMadera': listaTiposMadera})
