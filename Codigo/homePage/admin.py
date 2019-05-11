from django.contrib import admin
from homePage.models import infousuario
from homePage.models import FormatoLiterario
from homePage.models import GeneroLiterario
from homePage.models import infoLibro
from homePage.models import Carrito
from homePage.models import ArticulosComprados
from homePage.models import contenidoMultimedia
from homePage.models import GeneroManualidad
from homePage.models import contenidoManualidad
from homePage.models import Donacion
from homePage.models import Comentario
from homePage.models import competencias
from homePage.models import infoTarjeta

# Register your models here.
admin.site.register(infousuario)
admin.site.register(FormatoLiterario)
admin.site.register(GeneroLiterario)
admin.site.register(infoLibro)
admin.site.register(Carrito)
admin.site.register(ArticulosComprados)
admin.site.register(contenidoMultimedia)
admin.site.register(GeneroManualidad)
admin.site.register(contenidoManualidad)
admin.site.register(Donacion)
admin.site.register(Comentario)
admin.site.register(competencias)
admin.site.register(infoTarjeta)
