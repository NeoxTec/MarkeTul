from django.db import models

# Create your models here.

class Cuenta(models.Model):
    idCuenta = models.BigIntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    celular = models.CharField(max_length=10)
    passwordNuevo = models.CharField(max_length =15)
    passwordConfirmado = models.CharField(max_length =15)

class Direccion(models.Model):
    idDireccion = models.BigIntegerField(primary_key=True, auto_created=True)
    pais = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    ciudad = models.TextField(max_length=30)
    codigoPostal= models.CharField(max_length =5)
    direccion = models.TextField(max_length =50)
    idCuenta = models.ForeignKey(Cuenta, null=True, blank=True, on_delete=models.CASCADE)

