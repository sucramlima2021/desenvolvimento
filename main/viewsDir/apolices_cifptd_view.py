# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..formsDir.apolices_cifptd_Form import ApolicesCIFPTD, ApolicesCIFPTDForm, HistoricoCIFPTD, HistoricoCIFPTDForm
def apolicesCIFPTD_list(request):
    return base_list_view(
        request,
        model=ApolicesCIFPTD,
        template_name='apolicesCIFPTD_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def apolicesCIFPTD_create(request):
    return base_create_view(
        request,
        form_class=ApolicesCIFPTDForm,
        success_url='apolicesCIFPTD_list',
        template_name='apolicesCIFPTD_form.html',
        success_message='Registro criado com sucesso!'
    )

def apolicesCIFPTD_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=ApolicesCIFPTD,
        form_class=ApolicesCIFPTDForm,
        success_url='apolicesCIFPTD_list',
        template_name='apolicesCIFPTD_form.html',
        success_message='Registro atualizado com sucesso!'
    )

def h_apolicesCIFPTD_list(request):
    return base_list_view(
        request,
        model=HistoricoCIFPTD,
        template_name='h_apolicesCIFPTD_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def h_apolicesCIFPTD_create(request):
    return base_create_view(
        request,
        form_class=HistoricoCIFPTDForm,
        success_url='h_apolicesCIFPTD_list',
        template_name='h_apolicesCIFPTD_form.html',
        success_message='Registro criado com sucesso!'
    )

def h_apolicesCIFPTD_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=HistoricoCIFPTD,
        form_class=HistoricoCIFPTDForm,
        success_url='h_apolicesCIFPTD_list',
        template_name='h_apolicesCIFPTD_form.html',
        success_message='Registro atualizado com sucesso!'
    )
