from django import forms
from ..modelsDir.apolices_com_ifptd import *
from ..modelsDir.apolices_geral import *
class ApolicesCIFPTDForm(forms.ModelForm):
    class Meta:
        model = ApolicesCIFPTD
        fields = '__all__'
        widgets = {
            'movimento': forms.RadioSelect(choices=ApolicesCIFPTD.STATUS_CHOICES,attrs={'class': 'form-check-input'}),
            'movimentoconjuge': forms.RadioSelect(choices=ApolicesCIFPTD.STATUS_CHOICES, attrs={'class': 'form-check-input'}),
            'datacancelamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'datacancelamentoconjuge': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'averbacao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'averbacaoconjuge': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'producao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'producaooconjuge': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'iniciooconjuge': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigenciaoconjuge': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        exclude = ('cliente',)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        
        
        self.fields["apolice"].queryset = ApolicesGerais.objects.filter(tipo='cifptd')