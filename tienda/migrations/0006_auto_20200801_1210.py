# Generated by Django 3.0.7 on 2020-08-01 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0004_administrador_correoadmin'),
        ('vendedor', '0013_solicitudesvendedor_noadmin'),
        ('tienda', '0005_direccion_iduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='tienda',
        ),
        migrations.AddField(
            model_name='carrito',
            name='idCons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Consumidor'),
        ),
        migrations.AddField(
            model_name='compras',
            name='idCons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Consumidor'),
        ),
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('idCarProd', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idCarrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Carrito')),
                ('idCatalogo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.Catalogo')),
                ('idProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dash.Producto')),
            ],
        ),
    ]
