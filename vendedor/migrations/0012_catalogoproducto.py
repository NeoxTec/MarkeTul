# Generated by Django 3.0.7 on 2020-07-10 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dash', '0004_administrador_correoadmin'),
        ('vendedor', '0011_catalogo_idtien'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoProducto',
            fields=[
                ('idCatProd', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idCatalogo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.Catalogo')),
                ('idProducto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dash.Producto')),
            ],
        ),
    ]
