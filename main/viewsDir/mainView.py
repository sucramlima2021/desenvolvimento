# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from ..models import *
from ..formsDir.clientesForm import ClientesForm
def principal(request):
    return base_list_view(
        request,
        model=Clientes,
        template_name='main.html',
        titulo = "Listagem de Clientes",
        campos_visiveis=['nome', 'cpf', 'controle'],
        url_edicao = 'seleciona_cliente',
        url_novo = 'clientes_create',
        url_apagar = 'clientes_delete',
        search_fields=['nome', 'cpf'],
        paginate_by=10  # Quantidade de registros por página
    )

def base_list_view(request, model, template_name, titulo, campos_visiveis, url_edicao, url_novo, search_fields=None, paginate_by=10, url_apagar = False):
    """
    View base para listar registros com busca e paginação.
    """
    query = request.GET.get('q')
    registros = model.objects.all()
    

    if query and search_fields:
        q_objects = Q()
        for field in search_fields:
            q_objects |= Q(**{f"{field}__icontains": query})
        registros = registros.filter(q_objects)

    # Paginação
    paginator = Paginator(registros, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    campos_busca = ", ".join([field.capitalize() for field in search_fields]) if search_fields else ""

    
    reg = []
    for registro in page_obj.object_list:
        
        reg.append({
            'cliente':registro,
            'cifptd':ApolicesCIFPTD.objects.filter(cliente = registro).exists(),
            'sifptd':ApolicesSIFPTD.objects.filter(cliente = registro).exists(),
            'mulher':ApolicesM.objects.filter(cliente = registro).exists(),
            'educ':ApolicesE.objects.filter(cliente = registro).exists(),
            'decesso':Decesso.objects.filter(cliente = registro).exists(), 
            })
      
    context = {
        'page_obj': page_obj,
        'registros': reg,
        'query': query,
        'title': titulo,
        'campos_visiveis': campos_visiveis,
        'url_edicao': url_edicao,
        'url_novo': url_novo,
        'url_apagar': url_apagar,
        'campos_busca': campos_busca
    }
    return render(request, template_name, context)