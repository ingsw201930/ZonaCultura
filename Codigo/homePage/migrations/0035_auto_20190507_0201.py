# Generated by Django 2.2 on 2019-05-07 07:01

from django.db import migrations, models
import homePage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0034_auto_20190503_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='infolibro',
            name='archivo',
            field=models.FileField(default='images/books/covers/default.pdf', upload_to='contenido/books/', validators=[homePage.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='contenidomanualidad',
            name='puntaje',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
