# Generated by Django 2.2 on 2019-05-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0059_auto_20190513_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenidomanualidad',
            name='tipo',
            field=models.CharField(choices=[('es', 'escultura'), ('pin', 'pintura')], max_length=2, null=True),
        ),
    ]
