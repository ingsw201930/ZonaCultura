# Generated by Django 2.2 on 2019-05-22 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0080_infousuario_numerotelefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infousuario',
            name='numeroTelefono',
            field=models.PositiveIntegerField(blank=True, max_length=20, null=True),
        ),
    ]