# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view

from ..formsDir.apolices_mulher_Form import ApolicesM, ApolicesMForm, HistoricoM, HistoricoMForm
def apolicesM_list(request):
    return base_list_view(
        request,
        model=ApolicesM,
        template_name='apolicesM_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def apolicesM_create(request):
    return base_create_view(
        request,
        form_class=ApolicesMForm,
        success_url='apolicesM_list',
        template_name='apolicesM_form.html',
        success_message='Registro criado com sucesso!'
    )

def apolicesM_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=ApolicesM,
        form_class=ApolicesMForm,
        success_url='apolicesM_list',
        template_name='apolicesM_form.html',
        success_message='Registro atualizado com sucesso!'
    )

def h_apolicesM_list(request):
    return base_list_view(
        request,
        model=HistoricoM,
        template_name='h_apolicesM_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def h_apolicesM_create(request):
    return base_create_view(
        request,
        form_class=HistoricoMForm,
        success_url='h_apolicesM_list',
        template_name='h_apolicesM_form.html',
        success_message='Registro criado com sucesso!'
    )

def h_apolicesM_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=HistoricoM,
        form_class=HistoricoMForm,
        success_url='h_apolicesM_list',
        template_name='h_apolicesM_form.html',
        success_message='Registro atualizado com sucesso!'
    )
