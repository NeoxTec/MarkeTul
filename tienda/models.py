from django.db import models
from django.contrib.auth.models import User
from admin_dash.models import Producto
from vendedor.models import CatalogoProducto, Vendedor, Catalogo

# Create your models here.

class Consumidor(models.Model):
    idConsumidor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    pw = models.CharField(max_length =15, null=True)
    telefono = models.CharField(max_length=15)
    idUser = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class Forma_Pago(models.Model):
    idForma_pago = models.AutoField(primary_key=True)
    nombre_propietario = models.CharField(max_length=50)
    numero_tarjeta = models.CharField(max_length=16)
    mes_vencimiento = models.CharField(max_length=3,null=True,blank=True)
    anio_vencimiento = models.CharField(max_length=3,null=True,blank=True)
    tipo_pago = models.CharField(max_length=20, null=True,blank=True)
    idUser = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

# Añadir forma de pago en efectivo y Paypal

class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=30,null=True, blank=True,)
    colonia = models.CharField(max_length=30,null=True, blank=True,)
    codigoPostal= models.CharField(max_length =7,null=True, blank=True,)
    numeroExterior= models.CharField(max_length =7, null=True, blank=True,)
    numeroInterior= models.CharField(max_length =7, null=True, blank=True,)
    idUser = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

# Añadir tabla visual de las direcciones

class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(null=True, blank=True)
    subtotal = models.FloatField(null=True, blank=True)
    idCons = models.ForeignKey(Consumidor, null=True, blank=True,on_delete=models.CASCADE)

class CarritoProducto(models.Model):
    idCarProd = models.AutoField(primary_key=True,auto_created=True)
    idProducto = models.ForeignKey(Producto,null=True, blank=True, on_delete=models.CASCADE)
    idCatalogo = models.ForeignKey(Catalogo,null=True, blank=True, on_delete=models.CASCADE)
    idCarrito = models.ForeignKey(Carrito, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.SmallIntegerField(null=True, blank=True)
    
class Compras(models.Model):
    idCompra = models.AutoField(primary_key=True)
    total = models.IntegerField(null=True,blank=True) 
    fecha = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    idCons = models.ForeignKey(Consumidor, null=True, blank=True,on_delete=models.CASCADE)
    idForma_pago = models.ForeignKey(Forma_Pago, null=True, blank=True, on_delete=models.CASCADE)

class ProductoComprado(models.Model):
    idProCom = models.AutoField(primary_key=True)
    idCompra = models.ForeignKey(Compras, null=True,blank=True, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto,null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.SmallIntegerField(null=True, blank=True)

"""class Pedido(models.Model):
    idPedido = models.CharField(max_length=200,null=True)
    idProducto_pedido = models.ForeignKey(Producto,null=True, blank=True, on_delete=models.CASCADE)
    idCatalogo = models.ForeignKey(Catalogo, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.SmallIntegerField(null=True, blank=True)"""