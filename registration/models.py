from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tipo_usuario(models.Model):
    idTipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=200)

class Usuario_Tipo(models.Model):
    idUser = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    idTipo_User = models.ForeignKey(Tipo_usuario,null=True, blank=True, on_delete=models.CASCADE)
