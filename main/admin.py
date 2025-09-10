from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

#admin.site.register(Clientes)
admin.site.register(ApolicesCIFPTD)
admin.site.register(ApolicesSIFPTD)
admin.site.register(ApolicesGerais)
admin.site.register(ApolicesM)
admin.site.register(ApolicesE)
admin.site.register(Decesso)
admin.site.register(BeneficiariosNovos)
admin.site.register(Angariadores)
admin.site.register(Agregados)
admin.site.register(ApolicesResidencia)
admin.site.register(ApolicesVida)
admin.site.register(ApolicesMoto)
admin.site.register(ApolicesCarro)
admin.site.register(Sinistros)
admin.site.register(ApoliceBase)

@admin.register(Clientes)
class ClienteAdmin(SimpleHistoryAdmin):
    list_display = ("id", "nome", "cpf", "email")
    search_fields = ("nome", "cpf")
# Register your models here.
