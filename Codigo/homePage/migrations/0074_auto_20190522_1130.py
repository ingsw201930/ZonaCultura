# Generated by Django 2.2 on 2019-05-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0073_auto_20190522_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infolibro',
            name='tieneCuentaActivada',
        ),
        migrations.AddField(
            model_name='infousuario',
            name='tieneCuentaActivada',
            field=models.BooleanField(default=True),
        ),
    ]