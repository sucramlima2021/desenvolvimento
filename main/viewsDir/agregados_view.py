# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from ..models import Agregados
from ..formsDir.agregados_Form import AgregadosForm
def agregados_list(request):
    return base_list_view(
        request,
        model=Agregados,
        template_name='agregados_list.html',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def agregados_create(request):
    return base_create_view(
        request,
        form_class=AgregadosForm,
        success_url='agregados_list',
        template_name='agregados_form.html',
        success_message='Registro criado com sucesso!'
    )

def agregados_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=Agregados,
        form_class=AgregadosForm,
        success_url='agregados_list',
        template_name='agregados_form.html',
        success_message='Registro atualizado com sucesso!'
    )
