# Generated by Django 2.2 on 2019-04-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0016_auto_20190414_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infotarjeta',
            name='numeroCuotas',
        ),
        migrations.AlterField(
            model_name='infousuario',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
