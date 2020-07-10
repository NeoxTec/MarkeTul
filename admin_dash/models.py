from django.db import models

# Create your models here.
class Administrador(models.Model):
    nombreAdmin = models.CharField(max_length=120)
    telefonoAdmin = models.CharField(max_length=12)
    direccionAdmin = models.CharField(max_length=200)

class Tienda(models.Model):
    idTi = models.BigIntegerField(primary_key=True,auto_created=True)
    nombreTi = models.CharField(max_length=200)
    logoTi = models.ImageField(upload_to="tienda")
    idAdmin = models.ForeignKey(Administrador, null=True, on_delete=models.SET_NULL)

class Producto(models.Model):
    idProd = models.BigIntegerField(primary_key=True, auto_created=True)
    nombreProd = models.CharField(max_length=200)
    descripcionProd = models.TextField()
    marcaProd = models.CharField(max_length=200)
    categoriaProd = models.CharField(max_length=120)
    precioProd = models.DecimalField(decimal_places=2,max_digits=7)
    medidasProd = models.TextField()
    existenciasProd = models.IntegerField()
    idTi = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
