from django.contrib import admin

from associados.models import Associado,Endereco,Contato,SituacaoAssociado

admin.site.register(Associado)
admin.site.register(Endereco)
admin.site.register(Contato)
admin.site.register(SituacaoAssociado)
# Register your models here.
