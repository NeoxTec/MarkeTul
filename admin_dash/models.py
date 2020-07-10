from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Administrador(models.Model):
    #idAdmin = models.AutoField(primary_key=True)
    nombreAdmin = models.CharField(max_length=120)
    telefonoAdmin = models.CharField(max_length=12, null= True)
    direccionAdmin = models.CharField(max_length=200)
    idUser = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)

class Tienda(models.Model):
    idTi = models.AutoField(primary_key=True)
    nombreTi = models.CharField(max_length=200)
    logoTi = models.ImageField(upload_to="tienda",null=True)
    idAdmin = models.ForeignKey(Administrador, null=True, on_delete=models.CASCADE)

class Producto(models.Model):
    idProd = models.AutoField(primary_key=True)
    nombreProd = models.CharField(max_length=200)
    descripcionProd = models.TextField()
    marcaProd = models.CharField(max_length=200)
    categoriaProd = models.CharField(max_length=120)
    precioProd = models.DecimalField(decimal_places=2,max_digits=7)
    medidasProd = models.TextField()
    existenciasProd = models.IntegerField()
    imagenProd = models.ImageField(upload_to="productos", null=True)
    estado= models.BooleanField(default=1)
    idTi = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
