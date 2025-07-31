# views/a2055_views.py
from .base_views import base_list_view, base_create_view, base_update_view
from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from ..models import Clientes, ApolicesCIFPTD, ApolicesSIFPTD, ApolicesM, ApolicesE, Decesso
from ..formsDir.clientesForm import ClientesForm
def clientes_list(request):
    return base_list_view(
        request,
        model=Clientes,
        template_name='main.html',
        titulo = "Listagem de Clientes",
        campos_visiveis=['nome', 'cpf', 'controle'],
        url_edicao = 'clientes_update',
        url_novo = 'clientes_create',
        url_apagar = 'clientes_delete',
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
    
def show_cliente(request, pk):
    if not pk:
        return HttpResponse(request, 'ID não fornecido na URL.')
    cliente = get_object_or_404(Clientes, id=pk)
    
    campos = []
    for field in cliente._meta.get_fields():
        if field.concrete and not field.many_to_many and not field.one_to_many:
            
            valor = getattr(cliente, field.name)
            # Para campos com choices, pegar display:
            if field.choices:
                valor = getattr(cliente, f'get_{field.name}_display')()
            campos.append((field.name, valor))

    return render(request, 'show_cliente.html', {'cliente': cliente, 'campos': campos})

def clientes_delete(request, pk):
    cliente = Clientes.objects.get(id = pk)
    if cliente:
        cliente.delete()
    return redirect(clientes_list)

def seleciona_cliente(request, pk):
    if not pk:
        return HttpResponse(request, 'ID não fornecido na URL.')
    cliente = get_object_or_404(Clientes, id=pk)
    
    cifptd = ApolicesCIFPTD.objects.filter(cliente = cliente)
    sifptd = ApolicesSIFPTD.objects.filter(cliente = cliente)
    mulher = ApolicesM.objects.filter(cliente = cliente)
    educ = ApolicesE.objects.filter(cliente = cliente)
    decesso = Decesso.objects.filter(cliente = cliente)
    
    apolices = {
            'Com IFPTD':{'tem':cifptd.exists(), 'apol':cifptd},
            'Sem IFPTD':{'tem':sifptd.exists(), 'apol':sifptd},
            'Mulher':{'tem':mulher.exists(), 'apol':mulher},
            'Educacional':{'tem':educ.exists(), 'apol':educ},
            'Decesso':{'tem':decesso.exists(), 'apol':decesso}, 
            }
    premioTotal = sum(
        (ap.premio or 0) + (getattr(ap, 'premioconjuge', 0)) 
        for info in apolices.values()
        for ap in info['apol']
    )
    isTotal = sum(
        ap.isbasica or 0
        for info in apolices.values()
        for ap in info['apol']
    )
    
    isConjugeTotal = sum(
        getattr(ap, 'premioconjuge', 0) or 0
        for info in apolices.values()
        for ap in info['apol']
    )
    
    
    return render(request, 'cliente.html', {'cliente': cliente, 'apolices': apolices, 'premio':premioTotal, 'isTotal':isTotal, 'isConj':isConjugeTotal })