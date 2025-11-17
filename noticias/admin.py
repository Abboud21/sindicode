from django.contrib import admin

from noticias.models import Categoria, Autor, Noticia

admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Noticia)
# Register your models here.