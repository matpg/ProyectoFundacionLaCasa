# Generated by Django 2.2.2 on 2019-06-25 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundacion', '0002_auto_20190624_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voluntario',
            name='fecha_nac',
        ),
    ]
