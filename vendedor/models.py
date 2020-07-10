from django.db import models
from admin_dash.models import Tienda
from django.contrib.auth.models import User

# Create your models here.
class SolicitudesVendedor(models.Model):
    idSolVen = models.BigIntegerField(primary_key=True,auto_created=True)
    motivos = models.TextField()
    status = models.SmallIntegerField()
    idTi = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
    idVen = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

