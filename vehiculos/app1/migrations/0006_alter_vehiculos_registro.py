# Generated by Django 5.1.3 on 2024-12-04 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_vehiculos_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='registro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.registroestacionamiento'),
        ),
    ]
