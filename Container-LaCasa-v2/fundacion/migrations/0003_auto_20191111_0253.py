# Generated by Django 2.2.6 on 2019-11-11 05:53

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('fundacion', '0002_voluntario_fecha_incripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id_proyecto', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('jefe', models.CharField(max_length=50)),
                ('fecha_inicio', models.CharField(max_length=20)),
                ('fecha_termino', models.CharField(max_length=20)),
                ('cantidad_voluntarios', models.IntegerField()),
                ('presupuesto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelManagers(
            name='voluntario',
            managers=[
                ('voluntarios', django.db.models.manager.Manager()),
            ],
        ),
    ]
