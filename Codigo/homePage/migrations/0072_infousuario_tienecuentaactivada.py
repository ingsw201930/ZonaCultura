# Generated by Django 2.2 on 2019-05-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0071_auto_20190521_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='infousuario',
            name='tieneCuentaActivada',
            field=models.BooleanField(default=True),
        ),
    ]