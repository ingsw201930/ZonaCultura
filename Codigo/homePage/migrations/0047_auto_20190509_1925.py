# Generated by Django 2.2 on 2019-05-10 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0046_auto_20190509_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infotarjeta',
            name='apellidoTitular',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='infotarjeta',
            name='codigoSeguridad',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='infotarjeta',
            name='fechaExpiración',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='infotarjeta',
            name='nombreTitular',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='infotarjeta',
            name='numeroTarjeta',
            field=models.IntegerField(max_length=8),
        ),
    ]
