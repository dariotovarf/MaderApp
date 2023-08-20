from django.db import models

# Create your models here.
class TipoMadera(models.Model):
    idTipoMadera = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    valorPie = models.PositiveIntegerField()

    def __str__(self):
        txt = "{0} {1} ${2}"
        return txt.format(self.idTipoMadera, self.nombre, self.valorPie)
    

class LotesMadera(models.Model):
    idLote = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)


class PiezaMadera(models.Model):
    idPieza = models.AutoField(primary_key=True)
    tipoMadera = models.ForeignKey(TipoMadera, null=True, on_delete=models.CASCADE)
    alto = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name="Alto")
    ancho = models.PositiveSmallIntegerField(null= False, blank=False, verbose_name="Ancho")
    largo = models.PositiveSmallIntegerField(null= False, blank=False, verbose_name="Largo")
    valorPieza = models.PositiveSmallIntegerField(null= True, blank=True)
    idLote = models.ForeignKey(LotesMadera, null=True, blank=True, on_delete=models.CASCADE)

    def totalValorPieza(self, valorPie):
        volumen = int(self.alto)*int(self.ancho)*int(self.largo)
        pieCubico = 0.000579 # 1 pulgada cubica equivale a 0.000579 pies cubicos
        return int(volumen*pieCubico*valorPie)
    
    def __str__(self):
        txt = "Id: {0} - Alto: {1} - Ancho :{2} - Largo : {3} - Valor Pieza : {4} - Id Lote :{5}"
        return txt.format(self.idPieza, self.alto, self.ancho, self.largo, self.valorPieza, self.idLote)
        

