# Generated by Django 3.0.7 on 2020-11-15 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0012_remove_compras_idforma_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='status',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
