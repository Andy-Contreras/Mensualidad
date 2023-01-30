# Generated by Django 4.1.5 on 2023-01-29 02:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('apellido', models.CharField(max_length=200, unique=True)),
                ('genero', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Femenino')])),
                ('Cedula', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('Edad', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de nacimientos')),
            ],
        ),
    ]
