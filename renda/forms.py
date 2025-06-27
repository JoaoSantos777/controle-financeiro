from django import forms
from .models import Renda
from categoria_renda.models import CategoriaRenda

class RendaForm(forms.ModelForm):
    class Meta:
        model = Renda
        fields = ['nome', 'categoria', 'valor', 'valor_disponivel', 'data_recebimento']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # captura o user passado na view
        super().__init__(*args, **kwargs)
        # filtra as categorias só do usuário logado
        self.fields['categoria'].queryset = CategoriaRenda.objects.filter(user=user)
