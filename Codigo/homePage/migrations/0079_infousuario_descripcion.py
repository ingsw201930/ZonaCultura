# Generated by Django 2.2 on 2019-05-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0078_compradores_multimedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='infousuario',
            name='descripcion',
            field=models.TextField(default='', max_length=130),
        ),
    ]
