# Generated by Django 2.2 on 2019-05-22 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0068_contrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenidomanualidad',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='images/manualidades/covers/'),
        ),
    ]