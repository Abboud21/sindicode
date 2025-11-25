
from django.urls import path
from noticias.views import index, autores, noticias, buscar, detalhe_noticia, todas_noticias, categoria

urlpatterns = [
    path('',noticias,name='index'),
    path('autor/',autores),
    path('buscar',buscar,name='buscar'),
    path('<int:noticia_id>/',detalhe_noticia,name='detalhe_noticia'),
    path('noticias/', todas_noticias, name='todas_noticias'),
    path('categoria/<int:categoria_id>/', categoria, name='categoria'),
]
