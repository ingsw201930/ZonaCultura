# Generated by Django 2.2 on 2019-05-10 01:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0052_auto_20190509_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infotarjeta',
            name='fechaExpiración',
        ),
        migrations.AddField(
            model_name='infotarjeta',
            name='anoExpiracion',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AddField(
            model_name='infotarjeta',
            name='mesExpiracion',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='infotarjeta',
            name='codigoSeguridad',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(900)]),
        ),
        migrations.AlterField(
            model_name='infotarjeta',
            name='numeroTarjeta',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9000000000000000)]),
        ),
    ]