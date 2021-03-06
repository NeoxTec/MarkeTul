# Generated by Django 3.0.7 on 2020-07-10 03:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_dash', '0002_auto_20200709_2014'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudesVendedor',
            fields=[
                ('idSolVen', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('motivos', models.TextField()),
                ('status', models.SmallIntegerField()),
                ('idTi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dash.Tienda')),
                ('idVen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
