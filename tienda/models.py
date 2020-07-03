from django.db import models

# Create your models here.

class Compras(models.Model):
    idCompra = models.BigIntegerField(primary_key=True, auto_created=True)
    producto = models.CharField(max_length=100)
    tienda = models.CharField(max_length=50)
    cantidad = models.IntegerField()   

class Forma_Pago(models.Model):
    idForma_pago = models.BigIntegerField(primary_key=True, auto_created=True)
    nombre_propietario = models.CharField(max_length=50)
    numero_tarjeta = models.IntegerField()
    vencimiento_dia = models.DateField()
    vencimiento_mes = models.DateField()
    vencimiento_anio = models.DateField()
