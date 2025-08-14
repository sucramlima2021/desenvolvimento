# views/a2055_views.py
# views.py
from datetime import date
from decimal import Decimal
from itertools import chain
from django.db.models import Q, F, Sum, Value, DecimalField, ExpressionWrapper
from django.db.models.functions import Coalesce
from django.shortcuts import render, HttpResponse

# IMPORTS alinhados aos seus arquivos
from ..models import *
# Constantes de status conforme STATUS_CHOICES nas suas models

def dashboard(request):
    #  TOTAL DE APÓLICES ATIVAS POR TIPO =====
    tipos = ApolicesGerais.TIPOS
    ativas_por_tipo=[]
    for tipo in tipos:
        apolices = ApoliceBase.objects.filter(movimento='A', apolice__tipo=tipo[0])
        ativas_por_tipo.append({'tipo':tipo[1], 'total':len(apolices)})

    # TOTAL DE PRÊMIO (geral) 
    premio_total = ApoliceBase.objects.filter(movimento='A').aggregate(total=Sum('premio'))['total'] or Decimal('0')

    premioc_total = Decimal('0')

    premioc_total += ApolicesCIFPTD.objects.filter(movimentoconjuge='A').aggregate(total=Sum('premioconjuge'))['total'] or Decimal('0')
    premioc_total += ApolicesSIFPTD.objects.filter(movimentoconjuge='A').aggregate(total=Sum('premioconjuge'))['total'] or Decimal('0')

    total_premio_geral = premio_total + premioc_total
    
    # top 10 apólices em uma lista com a soma prêmio+conjuge
    DEC = DecimalField(max_digits=18, decimal_places=2)
    
    total_expr = (
        Coalesce(F('premio'), Value(Decimal('0.00')), output_field=DEC)
        + Coalesce(F('apolicescifptd__premioconjuge'), Value(Decimal('0.00')), output_field=DEC)
        + Coalesce(F('apolicessifptd__premioconjuge'), Value(Decimal('0.00')), output_field=DEC)
    )

    # 1) Anota total por apólice
    # 2) Agrupa por tipo e soma o total
    qs = (
        ApoliceBase.objects
        .filter(movimento='A')  # apenas apólices ativas
        .annotate(total_apolice=ExpressionWrapper(total_expr, output_field=DEC))
        .values('apolice__tipo')  # agrupa por tipo do catálogo
        .annotate(total_tipo=Sum('total_apolice'))
        .order_by('-total_tipo')  # opcional: ranking por tipo
    )

    # Map para exibir rótulo amigável
    tipos_map = dict(ApolicesGerais.TIPOS)

    # Constrói lista final já com rótulo e código
    top10_apolices_por_premio = [
        {
            'tipo': tipos_map.get(row['apolice__tipo'], row['apolice__tipo']),
            'total': row['total_tipo'],
        }
        for row in qs
    ]
    
    
    
    
    # ANIVERSARIANTES DO DIA (clientes com apólice ativa) =====
    hoje = date.today()
    aniversariantes = ApoliceBase.objects.filter(movimento='A', cliente__nascimento__month=hoje.month, cliente__nascimento__day=hoje.day)

    #  Nº DE CLIENTES COM APÓLICES CANCELADAS OU SINISTRADAS =====
    cancelados =  ApoliceBase.objects.filter(movimento='C')
    sinistrados =  ApoliceBase.objects.filter(movimento='S')

    contexto = {
        "ativas_por_tipo": ativas_por_tipo,
        "total_premio_geral": total_premio_geral,
        "top10_apolices_por_premio": top10_apolices_por_premio,
        "aniversariantes_hoje": aniversariantes,
        "clientes_canceladas": len(cancelados),
        "clientes_sinistradas": len(sinistrados),
    }
    
    #return render(request, "inicio.html", contexto)
    return render(request, 'inicio.html', contexto)