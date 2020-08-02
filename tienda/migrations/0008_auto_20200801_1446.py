# Generated by Django 3.0.7 on 2020-08-01 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0004_administrador_correoadmin'),
        ('tienda', '0007_auto_20200801_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='idCarrito',
        ),
        migrations.AddField(
            model_name='compras',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ProductoComprado',
            fields=[
                ('idProCom', models.AutoField(primary_key=True, serialize=False)),
                ('idCompra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Compras')),
                ('idProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dash.Producto')),
            ],
        ),
    ]
