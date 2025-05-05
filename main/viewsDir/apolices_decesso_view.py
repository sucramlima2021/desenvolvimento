# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..formsDir.apolices_decesso_Form import DecessoForm, HistoricoDecessoForm, Decesso, HistoricoDecesso
def decesso_list(request):
    return base_list_view(
        request,
        model=Decesso,
        template_name='decesso_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def decesso_create(request):
    return base_create_view(
        request,
        form_class=DecessoForm,
        success_url='decesso_list',
        template_name='decesso_form.html',
        success_message='Registro criado com sucesso!'
    )

def decesso_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=Decesso,
        form_class=DecessoForm,
        success_url='decesso_list',
        template_name='decesso_form.html',
        success_message='Registro atualizado com sucesso!'
    )
    
def h_decesso_list(request):
    return base_list_view(
        request,
        model=HistoricoDecesso,
        template_name='h_decesso_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def h_decesso_create(request):
    return base_create_view(
        request,
        form_class=HistoricoDecessoForm,
        success_url='h_decesso_list',
        template_name='h_decesso_form.html',
        success_message='Registro criado com sucesso!'
    )

def h_decesso_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=HistoricoDecesso,
        form_class=HistoricoDecessoForm,
        success_url='h_decesso_list',
        template_name='h_decesso_form.html',
        success_message='Registro atualizado com sucesso!'
    )
