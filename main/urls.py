from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('principal', principal, name='principal'),
    
    path('clientes', clientes_list, name='clientes_list'),
    path('clientes/cadastrar', clientes_create, name='clientes_create'),
    path('clientes/editar/<int:pk>/', clientes_update, name='clientes_update'),
    path('clientes/mostrar/<int:pk>/', seleciona_cliente, name='seleciona_cliente'),
    path('clientes/apagar/<int:pk>/', clientes_delete, name='clientes_delete'),
    
    path('agregados', agregados_list, name='agregados_list'),
    path('agregados/cadastrar', agregados_create, name='agregados_create'),
    path('agregados/editar/<int:pk>/', agregados_update, name='agregados_update'),
    
    path('beneficiarios', beneficiarios_list, name='beneficiarios_list'),
    path('beneficiarios/cadastrar', beneficiarios_create, name='beneficiarios_create'),
    path('beneficiarios/editar/<int:pk>/', beneficiarios_update, name='beneficiarios_update'),
    
    path('apolicesGerais', apolicesGerais_list, name='apolicesGerais_list'),
    path('apolicesGerais/cadastrar', apolicesGerais_create, name='apolicesGerais_create'),
    path('apolicesGerais/editar/<int:pk>/', apolicesGerais_update, name='apolicesGerais_update'),
    path('apolicesGerais/apagar/<int:pk>/', apolicesGerais_delete, name='apolicesGerais_delete'),
]