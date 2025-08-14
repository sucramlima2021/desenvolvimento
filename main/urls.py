from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('', dashboard, name='dashboard'),
    path('clientes', clientes, name='clientes'),
    path('clientes/cadastrar', clientes_create, name='clientes_create'),
    path('clientes/editar/<int:pk>/', clientes_update, name='clientes_update'),
    path('clientes/mostrar/<int:pk>/', seleciona_cliente, name='seleciona_cliente'),
    path('clientes/apagar/<int:pk>/', clientes_delete, name='clientes_delete'),
    
    path('clientes/<int:pk>/apolices/CIFPTD/cadastrar/', apolicesCIFPTD_create, name='apolicesCIFPTD_create'),
    path('clientes/apolices/CIFPTD/editar/<int:pk>/', apolicesCIFPTD_update, name='apolicesCIFPTD_update'),
    path('clientes/apolices/CIFPTD/apagar/<int:pk>/', clientes_delete, name='clientes_delete'),
    
    path('clientes/<int:pk>/apolices/SIFPTD/cadastrar/', apolicesSIFPTD_create, name='apolicesSIFPTD_create'),
    path('clientes/apolices/SIFPTD/editar/<int:pk>/', apolicesSIFPTD_update, name='apolicesSIFPTD_update'),
    path('clientes/apolices/SIFPTD/apagar/<int:pk>/', clientes_delete, name='clientes_delete'),
    
    path('clientes/<int:pk>/apolices/MULHER/cadastrar/', apolicesMulher_create, name='apolicesMulher_create'),
    path('clientes/apolices/MULHER/editar/<int:pk>/', apolicesMulher_update, name='apolicesMulher_update'),
    path('clientes/apolices/MULHER/apagar/<int:pk>/', clientes_delete, name='clientes_delete'),
    
    path('clientes/<int:pk>/apolices/EDUCACIONAL/cadastrar/', apolicesE_create, name='apolicesE_create'),
    path('clientes/apolices/EDUCACIONAL/editar/<int:pk>/', apolicesE_update, name='apolicesE_update'),
    path('clientes/apolices/EDUCACIONAL/apagar/<int:pk>/', clientes_delete, name='clientes_delete'),
    
    path('clientes/<int:pk>/apolices/DECESSO/cadastrar/', decesso_create, name='decesso_create'),
    path('clientes/apolices/DECESSO/editar/<int:pk>/', decesso_update, name='decesso_update'),
    path('clientes/apolices/DECESSO/apagar/<int:pk>/', clientes_delete, name='clientes_delete'),
    path('clientes/apolices/DECESSO/imprimir/<int:pk>/', decesso_impressao, name='decesso_impressao'),
    
    path('clientes/<int:pk>/incluir/', escolhe_apolice, name='escolhe_apolice'),
    
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
    
    path("sinistros/", sinistros_list, name="sinistros_list"),
    path("sinistros/novo/", sinistros_create, name="sinistros_create"),
    path("sinistros/<int:pk>/editar/", sinistros_update, name="sinistros_update"),
    path("sinistros/<int:pk>/excluir/", sinistros_delete, name="sinistros_delete"),
    
]