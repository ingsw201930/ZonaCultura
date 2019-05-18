# Generated by Django 2.2 on 2019-05-18 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0065_contactos_mensajes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioObraLiteraria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('califi', models.PositiveIntegerField(default=0)),
                ('comentario', models.TextField(default='', max_length=150)),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.infoLibro')),
                ('usuarioComentador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homePage.infousuario')),
            ],
        ),
    ]
