# Generated by Django 2.2.5 on 2019-11-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundacion', '0008_auto_20191122_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='id_proyecto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
