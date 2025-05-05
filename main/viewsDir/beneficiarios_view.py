# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..models import Beneficiarios
from ..formsDir.beneficiarios_Form import BeneficiariosForm
def beneficiarios_list(request):
    return base_list_view(
        request,
        model=Beneficiarios,
        template_name='beneficiarios_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def beneficiarios_create(request):
    return base_create_view(
        request,
        form_class=BeneficiariosForm,
        success_url='beneficiarios_list',
        template_name='beneficiarios_form.html',
        success_message='Registro criado com sucesso!'
    )

def beneficiarios_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=Beneficiarios,
        form_class=BeneficiariosForm,
        success_url='beneficiarios_list',
        template_name='beneficiarios_form.html',
        success_message='Registro atualizado com sucesso!'
    )
