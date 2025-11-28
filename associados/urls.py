from django.urls import path
from associados.views import associados, cadastro, login, editar_associado, deletar_associado

urlpatterns = [
    path('associados/', associados, name='associados'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),

    path('editar/', editar_associado, name='editar_associado'),
    path('deletar/', deletar_associado, name='deletar_associado'),
]
