# Generated by Django 3.0.7 on 2020-07-03 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAdmin', models.CharField(max_length=120)),
                ('telefonoAdmin', models.CharField(max_length=12)),
                ('direccionAdmin', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('idTi', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombreTi', models.CharField(max_length=200)),
                ('logoTi', models.ImageField(upload_to='')),
                ('idAdmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_dash.Administrador')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProd', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('nombreProd', models.CharField(max_length=200)),
                ('descripcionProd', models.TextField()),
                ('marcaProd', models.CharField(max_length=200)),
                ('categoriaProd', models.CharField(max_length=120)),
                ('precioProd', models.DecimalField(decimal_places=2, max_digits=7)),
                ('medidasProd', models.TextField()),
                ('existenciasProd', models.IntegerField()),
                ('idTi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dash.Tienda')),
            ],
        ),
    ]
