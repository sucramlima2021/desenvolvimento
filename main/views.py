from django.shortcuts import render, HttpResponse
from .viewsDir.clientesView import *
from .viewsDir.agregados_view import *
from .viewsDir.beneficiarios_view import *
from .viewsDir.apolices_geral_view import *
from .viewsDir.apolices_cifptd_view import *
from .viewsDir.apolices_sifptd_view import *
from .viewsDir.apolices_mulher_view import *
from .viewsDir.apolices_educacional_view import *
from .viewsDir.apolices_decesso_view import *
from .viewsDir.mainView import *
from .viewsDir.sinistros_views import *
from .viewsDir.apolices_vida_view import *
from .viewsDir.apolices_residencia_view import *
from .viewsDir.apolices_moto_view import *
from .viewsDir.apolices_carro_view import *

def main(request):
    return HttpResponse('Princ')