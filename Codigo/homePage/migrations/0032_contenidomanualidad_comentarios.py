# Generated by Django 2.2 on 2019-05-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0031_contenidomanualidad_calificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenidomanualidad',
            name='comentarios',
            field=models.ManyToManyField(related_name='_contenidomanualidad_comentarios_+', to='homePage.contenidoManualidad'),
        ),
    ]
