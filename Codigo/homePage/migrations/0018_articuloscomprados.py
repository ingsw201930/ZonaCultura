# Generated by Django 2.2 on 2019-04-15 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0017_auto_20190415_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticulosComprados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.infoLibro')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.infousuario')),
            ],
        ),
    ]