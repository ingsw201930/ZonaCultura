# Generated by Django 2.2 on 2019-04-15 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0017_auto_20190415_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infotarjeta',
            name='numeroCuotas',
        ),
    ]
