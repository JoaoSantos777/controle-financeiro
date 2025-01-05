from django import forms
from .models import Renda
from categoria_renda.models import CategoriaRenda

class RendaForm(forms.ModelForm):
    class Meta:
        model = Renda
        fields = ['nome', 'categoria', 'valor', 'valor_disponivel', 'data_recebimento']
