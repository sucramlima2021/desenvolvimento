# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..formsDir.apolices_geral_Form import ApolicesGeralForm, ApolicesGerais
def apolicesGerais_list(request):
    return base_list_view(
        request,
        model=ApolicesGerais,
        template_name='apolicesGerais_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def apolicesGerais_create(request):
    return base_create_view(
        request,
        form_class=ApolicesGeralForm,
        success_url='apolicesGerais_list',
        template_name='apolicesGerais_form.html',
        success_message='Registro criado com sucesso!'
    )

def apolicesGerais_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=ApolicesGerais,
        form_class=ApolicesGeralForm,
        success_url='apolicesGerais_list',
        template_name='apolicesGerais_form.html',
        success_message='Registro atualizado com sucesso!'
    )
    
