# views/a2055_views.py
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from ..models import *
from ..formsDir.clientesForm import ClientesForm, Clientes
from .base_views import base_create_view, base_update_view
from .utils import get_diff 

def clientes(request):
    
    template_name='main.html'
    titulo = "Listagem de Clientes"
    campos_visiveis=['nome', 'cpf', 'matricula']
    url_edicao = 'clientes_update'
    url_novo = 'clientes_create'
    url_apagar = 'clientes_delete'
    search_fields=['nome', 'cpf']
    paginate_by=10
    query = request.GET.get('q')
    registros = Clientes.objects.all()
    if query and search_fields:
        q_objects = Q()
        for field in search_fields:
            q_objects |= Q(**{f"{field}__icontains": query})
        registros = registros.filter(q_objects)
    
    # Paginação
    paginator = Paginator(registros, paginate_by)
    print(paginator)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    campos_busca = ", ".join([field.capitalize() for field in search_fields]) if search_fields else ""
    
    reg = []
    try:
        for registro in page_obj.object_list:
            
            reg.append({
                'cliente':registro,
                'cifptd':ApolicesCIFPTD.objects.filter(cliente = registro).exists(),
                'sifptd':ApolicesSIFPTD.objects.filter(cliente = registro).exists(),
                'mulher':ApolicesM.objects.filter(cliente = registro).exists(),
                'educ':ApolicesE.objects.filter(cliente = registro).exists(),
                'decesso':Decesso.objects.filter(cliente = registro).exists(),
                'vida':ApolicesVida.objects.filter(cliente = registro).exists(),
                'residencia':ApolicesResidencia.objects.filter(cliente = registro).exists(),
                'carro':ApolicesCarro.objects.filter(cliente = registro).exists(),
                'moto':ApolicesMoto.objects.filter(cliente = registro).exists()
                })
    except:
        pass
    
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


def clientes_create(request):
    return base_create_view(
        request,
        form_class=ClientesForm,
        success_url='clientes',
        template_name='form_clientes.html',
        titulo = 'Cadastro de Clientes',
        success_message='Registro criado com sucesso!'
    )

def clientes_update(request, pk):
    return base_update_view(
        request,
        pk=pk,
        model=Clientes,
        form_class=ClientesForm,
        success_url='clientes',
        template_name='form_clientes.html',
        titulo = 'Dados do Cliente',
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
        try:
            cliente.delete()
        except:
            messages.error(request, "Não foi possível apagar este cliente. Existem registros vinculados a ele.")
            previous_url = request.META.get('HTTP_REFERER', '/')
            return redirect(previous_url)
    return redirect(clientes)

def seleciona_cliente(request, pk):
    if not pk:
        return HttpResponse(request, 'ID não fornecido na URL.')
    cliente = get_object_or_404(Clientes, id=pk)
    
    cifptd = ApolicesCIFPTD.objects.filter(cliente = cliente)
    sifptd = ApolicesSIFPTD.objects.filter(cliente = cliente)
    mulher = ApolicesM.objects.filter(cliente = cliente)
    educ = ApolicesE.objects.filter(cliente = cliente)
    decesso = Decesso.objects.filter(cliente = cliente)
    vida = ApolicesVida.objects.filter(cliente = cliente)
    residencia = ApolicesResidencia.objects.filter(cliente = cliente)
    carro = ApolicesCarro.objects.filter(cliente = cliente)
    moto = ApolicesMoto.objects.filter(cliente = cliente)
    apolices = {
            'CIFPTD':{'tem':cifptd.exists(), 'apol':cifptd},
            'SIFPTD':{'tem':sifptd.exists(), 'apol':sifptd},
            'MULHER':{'tem':mulher.exists(), 'apol':mulher},
            'EDUCACIONAL':{'tem':educ.exists(), 'apol':educ},
            'DECESSO':{'tem':decesso.exists(), 'apol':decesso}, 
            }
    
    apolices_diversas = {
        'VIDA':{'tem':vida.exists(), 'apol':vida},
        'RESIDENCIA':{'tem':residencia.exists(), 'apol':residencia},
        'MOTO':{'tem':moto.exists(), 'apol':moto},
        'CARRO':{'tem':carro.exists(), 'apol':carro},
    }
    
    premioTotal = sum(
        (getattr(ap, 'premio', 0) or 0) + (getattr(ap, 'premioconjuge', 0) or 0) 
        for info in apolices.values()
        for ap in info['apol']
    )
    isTotal = sum(
        getattr(ap, 'isbasica', 0) or 0
        for info in apolices.values()
        for ap in info['apol']
    )
    
    isConjugeTotal = sum(
        getattr(ap, 'premioconjuge', 0) or 0
        for info in apolices_diversas.values()
        for ap in info['apol']
    )
    
    premioTotalD = sum(
        (getattr(ap, 'premio', 0) or 0) + (getattr(ap, 'premioconjuge', 0) or 0) 
        for info in apolices_diversas.values()
        for ap in info['apol']
    )
    isTotalD = sum(
        getattr(ap, 'isbasica', 0) or 0
        for info in apolices_diversas.values()
        for ap in info['apol']
    )
    
    if not cifptd.exists() and not sifptd.exists() and not mulher.exists() and not educ.exists() and not decesso.exists():
        apolices = False
    
    if not vida.exists() and not residencia.exists() and not moto.exists():
        apolices_diversas = False
    
    return render(request, 'cliente.html', {'cliente': cliente, 
                                            'apolices': apolices, 
                                            'premio':premioTotal, 
                                            'isTotal':isTotal, 
                                            'isConj':isConjugeTotal, 
                                            'apolicesdiversas':apolices_diversas,
                                            'premioTotalD':premioTotalD,
                                            'isTotalD':isTotalD})
    

def escolhe_apolice(request, pk):
    cliente = get_object_or_404(Clientes, id=pk)
    cifptd = ApolicesGerais.objects.filter(tipo = 'cifptd')
    sifptd = ApolicesGerais.objects.filter(tipo = 'sifptd')
    mulher = ApolicesGerais.objects.filter(tipo = 'mulher')
    educacional = ApolicesGerais.objects.filter(tipo = 'educacional')
    return render(request, 'escolhe_apolice.html',{'cliente':cliente, 'cifptd':cifptd, 'sifptd':sifptd, 'mulher':mulher, 'educacional':educacional })


def cliente_history(request, pk):
    cliente = get_object_or_404(Clientes, pk=pk)
    
    HISTORY_TYPE_LABELS = {
    "+": "Criado",
    "~": "Alterado",
    "-": "Excluído",
}

    historicos = {
        "Agregados": Agregados.history.filter(cliente=cliente).order_by("-history_date"),
        "VIDA1": ApolicesCIFPTD.history.filter(cliente=cliente).order_by("-history_date"),
        "VIDA2": ApolicesSIFPTD.history.filter(cliente=cliente).order_by("-history_date"),
        "Mulher": ApolicesM.history.filter(cliente=cliente).order_by("-history_date"),
        "Educacional": ApolicesE.history.filter(cliente=cliente).order_by("-history_date"),
        "Decesso": Decesso.history.filter(cliente=cliente).order_by("-history_date"),
        "Vida": ApolicesVida.history.filter(cliente=cliente).order_by("-history_date"),
        "Residência": ApolicesResidencia.history.filter(cliente=cliente).order_by("-history_date"),
        "Moto": ApolicesMoto.history.filter(cliente=cliente).order_by("-history_date"),
        "Carro": ApolicesCarro.history.filter(cliente=cliente).order_by("-history_date"),
        "Beneficiários": BeneficiariosNovos.history.filter(cliente=cliente).order_by("-history_date"),
        "Cadastro": cliente.history.all().order_by("-history_date")
    }

    # transforma cada registro em um dict com diff calculado
    historicos_com_diff = {}
    for nome, registros in historicos.items():
        if registros:
            historicos_com_diff[nome] = [
                {
                    "data": r.history_date,
                    "usuario": r.history_user,
                    "acao": HISTORY_TYPE_LABELS.get(r.history_type, r.history_type),
                    "diff": get_diff(r),
                }
                for r in registros
            ]

    return render(request, "cliente_historico.html", {
        "cliente": cliente,
        "historicos": historicos_com_diff
    })