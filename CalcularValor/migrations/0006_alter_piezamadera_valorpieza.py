# Generated by Django 3.2.8 on 2023-07-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalcularValor', '0005_piezamadera_idlote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piezamadera',
            name='valorPieza',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
