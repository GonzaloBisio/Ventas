# Generated by Django 2.2 on 2020-07-01 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedore',
            name='producto',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idd',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='ciudad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='comuna',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='numero',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idd',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='rut',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='proveedore',
            name='web',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='venta',
            name='descuento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='venta',
            name='idd',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='venta',
            name='montofinal',
            field=models.CharField(max_length=50),
        ),
    ]
