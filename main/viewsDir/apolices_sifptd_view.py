# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..models import ApolicesSIFPTD
from ..formsDir.apolices_sifptd_Form import ApolicesSIFPTD, ApolicesSIFPTDForm, HistoricoSIFPTD, HistoricoSIFPTDForm
def apolicesSIFPTD_list(request):
    return base_list_view(
        request,
        model=ApolicesSIFPTD,
        template_name='apolicesSIFPTD_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def apolicesSIFPTD_create(request):
    return base_create_view(
        request,
        form_class=ApolicesSIFPTDForm,
        success_url='apolicesSIFPTD_list',
        template_name='apolicesSIFPTD_form.html',
        success_message='Registro criado com sucesso!'
    )

def apolicesSIFPTD_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=ApolicesSIFPTD,
        form_class=ApolicesSIFPTDForm,
        success_url='apolicesSIFPTD_list',
        template_name='apolicesSIFPTD_form.html',
        success_message='Registro atualizado com sucesso!'
    )

def h_apolicesSIFPTD_list(request):
    return base_list_view(
        request,
        model=HistoricoSIFPTD,
        template_name='h_apolicesSIFPTD_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def h_apolicesSIFPTD_create(request):
    return base_create_view(
        request,
        form_class=HistoricoSIFPTDForm,
        success_url='h_apolicesSIFPTD_list',
        template_name='h_apolicesSIFPTD_form.html',
        success_message='Registro criado com sucesso!'
    )

def h_apolicesSIFPTD_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=HistoricoSIFPTD,
        form_class=HistoricoSIFPTDForm,
        success_url='h_apolicesSIFPTD_list',
        template_name='h_apolicesSIFPTD_form.html',
        success_message='Registro atualizado com sucesso!'
    )
