from django.shortcuts import render
from django.http import HttpResponse
from .viewsDir.clientesView import *
from .viewsDir.agregados_view import *
from .viewsDir.beneficiarios_view import *
from .viewsDir.apolices_geral_view import *
from .viewsDir.apolices_cifptd_view import *
from .viewsDir.apolices_cifptd_view import *
from .viewsDir.mainView import *
# Create your views here.
def main(request):
    return HttpResponse("pagina principal")
