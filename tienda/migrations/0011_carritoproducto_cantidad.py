# Generated by Django 3.0.7 on 2020-08-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_productocomprado_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoproducto',
            name='cantidad',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
