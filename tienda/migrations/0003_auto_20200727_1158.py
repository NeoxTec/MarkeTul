# Generated by Django 3.0.7 on 2020-07-27 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendedor', '0012_catalogoproducto'),
        ('admin_dash', '0004_administrador_correoadmin'),
        ('tienda', '0002_direccion_idcuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('idCatProd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.CatalogoProducto')),
                ('idProd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dash.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('idConsumidor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('pw', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
                ('idUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='idCuenta',
        ),
        migrations.RemoveField(
            model_name='direccion',
            name='pais',
        ),
        migrations.RemoveField(
            model_name='forma_pago',
            name='vencimiento_anio',
        ),
        migrations.RemoveField(
            model_name='forma_pago',
            name='vencimiento_dia',
        ),
        migrations.RemoveField(
            model_name='forma_pago',
            name='vencimiento_mes',
        ),
        migrations.AddField(
            model_name='compras',
            name='idForma_pago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Forma_Pago'),
        ),
        migrations.AddField(
            model_name='compras',
            name='idUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='direccion',
            name='calle',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='colonia',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='numeroExterior',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='numeroInterior',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='forma_pago',
            name='fvencimiento',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='forma_pago',
            name='idUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='compras',
            name='idCompra',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='codigoPostal',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='idDireccion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='forma_pago',
            name='idForma_pago',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='forma_pago',
            name='numero_tarjeta',
            field=models.CharField(max_length=16),
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
        migrations.AddField(
            model_name='compras',
            name='idCarrito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Carrito'),
        ),
    ]