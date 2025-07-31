# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..models import Agregados
from ..formsDir.agregados_Form import AgregadosForm

def agregados_list(request):
    return base_list_view(
        request,
        model=Agregados,
        template_name='list.html',
        titulo="Listagem de Agregados",
        campos_visiveis=['nome', 'cpf', 'parentesco'],
        url_edicao='agregados_update',
        url_novo='agregados_create',
        search_fields=['nome', 'cpf'],
        paginate_by=10
    )

def agregados_create(request):
    return base_create_view(
        request,
        form_class=AgregadosForm,
        success_url='agregados_list',
        template_name='form.html',
        titulo='Cadastro de Agregado',
        success_message='Agregado criado com sucesso!'
    )

def agregados_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=Agregados,
        form_class=AgregadosForm,
        success_url='agregados_list',
        template_name='form.html',
        titulo='Edição de Agregado',
        success_message='Agregado atualizado com sucesso!'
    )
