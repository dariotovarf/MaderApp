from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    listaPiezas= PiezaMadera.objects.filter(idLote = None)
    listaTiposMadera = TipoMadera.objects.all()
    total = 0
    for item in listaPiezas:
        total = total + item.valorPieza
    return render(request, 'home.html', {"listaPiezas" : listaPiezas, "listaTiposMadera" : listaTiposMadera, "total": total })

def calcularValorPieza(request):
    piezaMadera = PiezaMadera()
    tipoMadera = TipoMadera.objects.get(idTipoMadera=request.POST['tipoMadera'])
    piezaMadera.tipoMadera = tipoMadera
    piezaMadera.alto = request.POST['txtAlto']
    piezaMadera.ancho = request.POST['txtAncho']
    piezaMadera.largo = request.POST['txtLargo']
    tipoMadera = TipoMadera.objects.get(idTipoMadera = request.POST['tipoMadera'])
    piezaMadera.valorPieza = piezaMadera.totalValorPieza(tipoMadera.valorPie)
    piezaMadera = PiezaMadera.objects.create(tipoMadera=piezaMadera.tipoMadera, alto=piezaMadera.alto, ancho=piezaMadera.ancho, largo=piezaMadera.largo, valorPieza=piezaMadera.valorPieza, idLote=None)
    listaPiezas= PiezaMadera.objects.filter(idLote = None)
    listaTiposMadera = TipoMadera.objects.all()
    total = 0
    for item in listaPiezas:
        total = total + item.valorPieza
    
    return render(request, 'home.html', {"listaPiezas" : listaPiezas, "listaTiposMadera" : listaTiposMadera, "total": total })

def eliminarPiezaMadera(request, idPieza):
    pieza = PiezaMadera.objects.get(idPieza=idPieza)
    pieza.delete()
    listaPiezas= PiezaMadera.objects.filter(idLote = None)
    listaTiposMadera = TipoMadera.objects.all()
    total = 0
    for item in listaPiezas:
        total = total + item.valorPieza
    return render(request, 'home.html', {"listaPiezas" : listaPiezas, "listaTiposMadera" : listaTiposMadera, "total": total })


def detallesPiezaMadera(request, piezaMadera):
    return render('detallesPiezaMadera.html', {"piezaMadera": piezaMadera})

def tiposMadera(request):
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'tiposMadera.html', {'listaTiposMadera': listaTiposMadera})

def edicionTipoMadera(request, idTipoMadera):
    tipoMadera = TipoMadera.objects.get(idTipoMadera=idTipoMadera)
    return render(request, 'edicionTipoMadera.html', {'tipoMadera': tipoMadera})

def editarTipoMadera(request):
    idTipoMadera = request.POST['txtIdTipoMadera']
    nombre = request.POST['txtNombre']
    valorPie = request.POST['txtValorPie']
    tipoMadera = TipoMadera.objects.get(idTipoMadera=idTipoMadera)
    tipoMadera.nombre = nombre
    tipoMadera.valorPie = valorPie
    tipoMadera.save()
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'tiposMadera.html', {'listaTiposMadera': listaTiposMadera})

def registrarTipoMadera(request):
    nombre = request.POST['txtNombre']
    valorPie = request.POST['txtValor']
    tipoMadera = TipoMadera.objects.create(nombre=nombre, valorPie=valorPie)
    messages.success(request, 'Tipo de Madera Registrada')
    listaTiposMadera = TipoMadera.objects.all()
    return render(request, 'tiposMadera.html', {'listaTiposMadera': listaTiposMadera})

def registrarLote(request):
    listaPiezas= PiezaMadera.objects.filter(idLote = None)
    lote = LotesMadera.objects.create()
    #pieza = PiezaMadera()
    idLote = lote.idLote
    for pieza in listaPiezas:
        pieza.idLote = lote
        pieza.save()
    
    listaPiezas= PiezaMadera.objects.filter(idLote = None)
    listaTiposMadera = TipoMadera.objects.all()
    total = 0
    for item in listaPiezas:
        total = total + item.valorPieza
    return render(request, 'home.html', {"listaPiezas" : listaPiezas, "listaTiposMadera" : listaTiposMadera, "total": total })

def listarLotesMaderaDetalles(request, idLote):
    print('paso 1')
    total = 0
    lote = LotesMadera.objects.get(idLote=idLote)
    listaPiezas = PiezaMadera.objects.filter(idLote = lote)
    listaLotesMadera = LotesMadera.objects.all()
    for item in listaPiezas:
        total = total + item.valorPieza
    return render(request, 'historialLotes.html', {'listaLotesMadera': listaLotesMadera, 'listaPiezas': listaPiezas, 'total': total})

def listarLotesMadera(request):
    listaLotesMadera = LotesMadera.objects.all()
    return render(request, 'historialLotes.html', {'listaLotesMadera': listaLotesMadera})