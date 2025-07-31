from .base_views import base_list_view, base_create_view, base_update_view
from ..models import Beneficiarios
from ..formsDir.beneficiarios_Form import BeneficiariosForm

def beneficiarios_list(request):
    return base_list_view(
        request,
        model=Beneficiarios,
        template_name='list.html',
        titulo="Listagem de Beneficiários",
        campos_visiveis=['nome', 'cpf', 'parentesco'],
        url_edicao='beneficiarios_update',
        url_novo='beneficiarios_create',
        search_fields=['nome', 'cpf'],
        paginate_by=10
    )

def beneficiarios_create(request):
    return base_create_view(
        request,
        form_class=BeneficiariosForm,
        success_url='beneficiarios_list',
        template_name='form.html',
        titulo='Cadastro de Beneficiário',
        success_message='Beneficiário criado com sucesso!'
    )

def beneficiarios_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=Beneficiarios,
        form_class=BeneficiariosForm,
        success_url='beneficiarios_list',
        template_name='form.html',
        titulo='Edição de Beneficiário',
        success_message='Beneficiário atualizado com sucesso!'
    )
