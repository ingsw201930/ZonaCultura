# Generated by Django 2.2 on 2019-05-07 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0036_remove_infolibro_formato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infolibro',
            name='archivo',
        ),
    ]
