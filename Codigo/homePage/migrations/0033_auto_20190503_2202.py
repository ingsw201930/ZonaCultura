# Generated by Django 2.2 on 2019-05-04 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0032_contenidomanualidad_comentarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenidomanualidad',
            name='comentarios',
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('califi', models.IntegerField(default=0)),
                ('comentario', models.TextField(default='', max_length=150)),
                ('manualidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.contenidoManualidad')),
                ('usuarioComentador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.infousuario')),
            ],
        ),
    ]
