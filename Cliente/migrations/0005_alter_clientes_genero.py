# Generated by Django 4.1.5 on 2023-01-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_alter_clientes_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='genero',
            field=models.IntegerField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M'),
        ),
    ]
