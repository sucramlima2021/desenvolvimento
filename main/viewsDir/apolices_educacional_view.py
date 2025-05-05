# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..models import ApolicesE
from ..formsDir.apolices_educacionais_Form import ApolicesEForm, ApolicesE, HistoricoE, HistoricoEForm
def apolicesE_list(request):
    return base_list_view(
        request,
        model=ApolicesE,
        template_name='apolicesE_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def apolicesE_create(request):
    return base_create_view(
        request,
        form_class=ApolicesEForm,
        success_url='apolicesE_list',
        template_name='apolicesE_form.html',
        success_message='Registro criado com sucesso!'
    )

def apolicesE_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=ApolicesE,
        form_class=ApolicesEForm,
        success_url='apolicesE_list',
        template_name='apolicesE_form.html',
        success_message='Registro atualizado com sucesso!'
    )
    
def h_apolicesE_list(request):
    return base_list_view(
        request,
        model=HistoricoE,
        template_name='h_apolicesE_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def h_apolicesE_create(request):
    return base_create_view(
        request,
        form_class=HistoricoEForm,
        success_url='h_apolicesE_list',
        template_name='h_apolicesE_form.html',
        success_message='Registro criado com sucesso!'
    )

def h_apolicesE_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=HistoricoE,
        form_class=HistoricoEForm,
        success_url='h_apolicesE_list',
        template_name='h_apolicesE_form.html',
        success_message='Registro atualizado com sucesso!'
    )
