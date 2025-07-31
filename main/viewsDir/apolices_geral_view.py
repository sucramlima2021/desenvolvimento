# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..formsDir.apolices_geral_Form import ApolicesGeralForm, ApolicesGerais
from django.shortcuts import redirect
def apolicesGerais_list(request):
    return base_list_view(
        request,
        model=ApolicesGerais,
        template_name='main.html',
        titulo = "Apólices Cadastradas",
        campos_visiveis=['nome', 'tipo'],
        url_edicao = 'apolicesGerais_update',
        url_novo = 'apolicesGerais_create',
        url_apagar = 'apolicesGerais_delete',
        search_fields=['nome', 'tipo'],
        paginate_by=10  # Quantidade de registros por página
    )

def apolicesGerais_create(request):
    return base_create_view(
        request,
        form_class=ApolicesGeralForm,
        success_url='apolicesGerais_list',
        template_name='form.html',
        titulo = 'Cadastro de Tipos de Apólices',
        success_message='Registro criado com sucesso!'
    )

def apolicesGerais_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=ApolicesGerais,
        form_class=ApolicesGeralForm,
        success_url='apolicesGerais_list',
        template_name='form.html',
        titulo = 'Alteração de Tipos de Apólices',
        success_message='Registro atualizado com sucesso!'
    )
    
def apolicesGerais_delete(request, pk):
    reg = ApolicesGerais.objects.get(id = pk)
    if reg:
        reg.delete()
    return redirect(apolicesGerais_list)
    
