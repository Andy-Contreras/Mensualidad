# Generated by Django 4.1.5 on 2023-01-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0003_alter_clientes_cedula_alter_clientes_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='genero',
            field=models.IntegerField(choices=[('M', 'Masculino'), ('F', 'Femenino')]),
        ),
    ]
