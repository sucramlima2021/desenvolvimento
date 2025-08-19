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
    path('clientes/apolices/CIFPTD/apagar/<int:pk>/', apolicesCIFPTD_delete, name='apolicesCIFPTD_delete'),
    
    path('clientes/<int:pk>/apolices/SIFPTD/cadastrar/', apolicesSIFPTD_create, name='apolicesSIFPTD_create'),
    path('clientes/apolices/SIFPTD/editar/<int:pk>/', apolicesSIFPTD_update, name='apolicesSIFPTD_update'),
    path('clientes/apolices/SIFPTD/apagar/<int:pk>/', apolicesSIFPTD_delete, name='apolicesSIFPTD_delete'),
    
    path('clientes/<int:pk>/apolices/MULHER/cadastrar/', apolicesMulher_create, name='apolicesMulher_create'),
    path('clientes/apolices/MULHER/editar/<int:pk>/', apolicesMulher_update, name='apolicesMulher_update'),
    path('clientes/apolices/MULHER/apagar/<int:pk>/', apolicesMulher_delete, name='apolicesMulher_delete'),
    
    path('clientes/<int:pk>/apolices/EDUCACIONAL/cadastrar/', apolicesE_create, name='apolicesE_create'),
    path('clientes/apolices/EDUCACIONAL/editar/<int:pk>/', apolicesE_update, name='apolicesE_update'),
    path('clientes/apolices/EDUCACIONAL/apagar/<int:pk>/', apolicesE_delete, name='apolicesE_delete'),
    
    path('clientes/<int:pk>/apolices/DECESSO/cadastrar/', decesso_create, name='decesso_create'),
    path('clientes/apolices/DECESSO/editar/<int:pk>/', decesso_update, name='decesso_update'),
    path('clientes/apolices/DECESSO/apagar/<int:pk>/', decesso_delete, name='decesso_delete'),
    path('clientes/apolices/DECESSO/imprimir/<int:pk>/', decesso_impressao, name='decesso_impressao'),
    
    path('clientes/<int:pk>/incluir/', escolhe_apolice, name='escolhe_apolice'),
    
    path('clientes/<int:pk>/agregados', agregados_list, name='agregados_list'),
    path('clientes/<int:pk>/agregados/cadastrar', agregados_create, name='agregados_create'),
    path('clientes/agregados/editar/<int:pk>/', agregados_update, name='agregados_update'),
    path('clientes/agregados/apagar/<int:pk>/', agregados_delete, name='agregados_delete'),
    
    path('beneficiarios', beneficiarios_list, name='beneficiarios_list'),
    path('beneficiarios/cadastrar', beneficiarios_create, name='beneficiarios_create'),
    path('beneficiarios/editar/<int:pk>/', beneficiarios_update, name='beneficiarios_update'),
    
    path('apolicesGerais', apolicesGerais_list, name='apolicesGerais_list'),
    path('apolicesGerais/cadastrar', apolicesGerais_create, name='apolicesGerais_create'),
    path('apolicesGerais/editar/<int:pk>/', apolicesGerais_update, name='apolicesGerais_update'),
    path('apolicesGerais/apagar/<int:pk>/', apolicesGerais_delete, name='apolicesGerais_delete'),
    
    path("sinistros/", sinistros_list, name="sinistros_list"),
    path("clientes/<int:pk>/sinistros/novo/", sinistros_create, name="sinistros_create"),
    path("clientes/sinistros/editar/<int:pk>/", sinistros_update, name="sinistros_update"),
    path("clientes/sinistros/excluir/<int:pk>/", sinistros_delete, name="sinistros_delete"),
    
    path('clientes/<int:pk>/apolices/VIDA/cadastrar/', apolicesVida_create, name='apolicesVida_create'),
    path('clientes/apolices/VIDA/editar/<int:pk>/', apolicesVida_update, name='apolicesVida_update'),
    path('clientes/apolices/VIDA/apagar/<int:pk>/', apolicesVida_delete, name='apolicesVida_delete'),
    path('clientes/apolices/VIDA/importar/', upload_pdf_vida, name='upload_pdf_vida'),
    
    path('clientes/<int:pk>/apolices/RESIDENCIA/cadastrar/', apolicesResidencia_create, name='apolicesResidencia_create'),
    path('clientes/apolices/RESIDENCIA/editar/<int:pk>/', apolicesResidencia_update, name='apolicesResidencia_update'),
    path('clientes/apolices/RESIDENCIA/apagar/<int:pk>/', apolicesResidencia_delete, name='apolicesResidencia_delete'),
    
    path('clientes/<int:pk>/apolices/MOTO/cadastrar/', apolicesMoto_create, name='apolicesMoto_create'),
    path('clientes/apolices/MOTO/editar/<int:pk>/', apolicesMoto_update, name='apolicesMoto_update'),
    path('clientes/apolices/MOTO/apagar/<int:pk>/', apolicesMoto_delete, name='apolicesMoto_delete'),
    
    path('clientes/<int:pk>/apolices/CARRO/cadastrar/', apolicesCarro_create, name='apolicesCarro_create'),
    path('clientes/apolices/CARRO/editar/<int:pk>/', apolicesCarro_update, name='apolicesCarro_update'),
    path('clientes/apolices/CARRO/apagar/<int:pk>/', apolicesCarro_delete, name='apolicesCarro_delete'),
    
]