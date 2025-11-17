from django.urls import path
from noticias.views import index, autores, noticias

urlpatterns = [
    path('',noticias),
    path('autor/',autores)
]