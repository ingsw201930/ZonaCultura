# Generated by Django 2.2 on 2019-04-15 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0016_auto_20190414_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infotarjeta',
            old_name='fechaExpiración',
            new_name='fechaExpiracion',
        ),
        migrations.AlterField(
            model_name='infousuario',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ArticulosComprados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.infoLibro')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.infousuario')),
            ],
        ),
    ]