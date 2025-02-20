# Generated by Django 5.0.6 on 2024-07-04 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='arrendador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inmuebles_en_arriendo', to='main.usuario'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='arrendatorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inmuebles_arrendados', to='main.usuario'),
        ),
    ]
