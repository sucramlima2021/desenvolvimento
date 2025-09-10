from django.db import models
from django_select2.forms import ModelSelect2Widget
from simple_history.models import HistoricalRecords

class Angariadores(models.Model):
    
    codigo = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    history = HistoricalRecords()
    
    def __str__(self):
        return str(f'{self.codigo} - {self.nome}')

class AngariadorSelectWidget(ModelSelect2Widget):
    model = Angariadores
    search_fields = ['nome__icontains', 'codigo__icontains']

    def label_from_instance(self, obj):
        return f'{obj.codigo} - {obj.nome}'