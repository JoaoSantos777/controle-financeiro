'''from django import forms
from .models import Politico

class PoliticoForm(forms.ModelForm):
    class Meta:
        model = Politico
        fields = ['nome', 'cpf', 'partido', 'cargo', 'email', 'telefone', 'data_nascimento']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

'''