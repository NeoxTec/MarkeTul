from django.db import models
from admin_dash.models import Tienda,Producto
from django.contrib.auth.models import User

# Create your models here.
class Vendedor(models.Model):
    idVend = models.AutoField(primary_key=True, auto_created=True)
    nombreVend = models.CharField(max_length=200)
    telefono = models.BigIntegerField(null=True, blank=True)
    correo = models.CharField(max_length=200, null=True, blank=True,)
    idUser = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class SolicitudesVendedor(models.Model):
    idSolVen = models.AutoField(primary_key=True,auto_created=True)
    motivos = models.TextField()
    edadVen = models.IntegerField(null=True,blank=True)
    genero = models.CharField(max_length=50, null=True,blank=True)
    nombreV = models.CharField(max_length=200, null=True)
    correoV = models.CharField(max_length=200, null=True, blank=True)
    direccionV = models.CharField(max_length=200, null=True)
    status = models.SmallIntegerField(default=0)
    idTi = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
    idVen = models.ForeignKey(Vendedor, null=True, blank=True, on_delete=models.CASCADE)

class Catalogo(models.Model):
    idCatal = models.AutoField(primary_key=True,auto_created=True)
    categoria = models.CharField(max_length=200)
    status = models.BooleanField(null=True, default=0)
    idVen = models.ForeignKey(Vendedor, null=True, blank=True, on_delete=models.CASCADE)
    idTien = models.ForeignKey(Tienda,null=True, blank=True, on_delete=models.CASCADE)

class CatalogoProducto(models.Model):
    idCatProd = models.AutoField(primary_key=True,auto_created=True)
    idProducto = models.ForeignKey(Producto,null=True, blank=True, on_delete=models.CASCADE)
    idCatalogo = models.ForeignKey(Catalogo,null=True, blank=True, on_delete=models.CASCADE)


