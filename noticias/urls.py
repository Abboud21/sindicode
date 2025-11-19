
from django.urls import path
from noticias.views import index, autores, noticias, buscar, detalhe_noticia

urlpatterns = [
    path('',noticias,name='index'),
    path('autor/',autores),
    path('buscar',buscar,name='buscar'),
    path('<int:noticia_id>/',detalhe_noticia,name='detalhe_noticia'),
]
