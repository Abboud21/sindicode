
from django.urls import path
from noticias.views import index, autores, noticias, buscar

urlpatterns = [
    path('',noticias),
    path('autor/',autores),
    path('buscar',buscar,name='buscar'),
]
