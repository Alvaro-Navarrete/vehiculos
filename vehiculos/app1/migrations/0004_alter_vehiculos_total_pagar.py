# Generated by Django 5.1.3 on 2024-11-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_vehiculos_total_pagar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='total_pagar',
            field=models.PositiveIntegerField(),
        ),
    ]