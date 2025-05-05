# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..models import Clientes
from ..formsDir.clientesForm import ClientesForm
def clientes_list(request):
    return base_list_view(
        request,
        model=Clientes,
        template_name='list.html',
        titulo = "Listagem de Clientes",
        campos_visiveis=['nome', 'cpf', 'controle'],
        url_edicao = 'clientes_update',
        url_novo = 'clientes_create',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def clientes_create(request):
    return base_create_view(
        request,
        form_class=ClientesForm,
        success_url='clientes_list',
        template_name='form.html',
        titulo = 'Cadastro de Clientes',
        success_message='Registro criado com sucesso!'
    )

def clientes_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=Clientes,
        form_class=ClientesForm,
        success_url='clientes_list',
        template_name='form.html',
        titulo = 'Edição do registro de Clientes',
        success_message='Registro atualizado com sucesso!'
    )
