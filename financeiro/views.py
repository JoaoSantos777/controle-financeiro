'''from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Politico, Partido, CategoriaDespesa, Despesa
from .forms import PoliticoForm



def index(request):
    context = {}
    return render(request, 'index.html', context)

# Politico
class PoliticoListView(ListView):
    model = Politico
    template_name = 'politico_list.html'
    context_object_name = 'politicos'

    def get_queryset(self):
        return Politico.objects.all()



class PoliticoCreateView(CreateView):
    model = Politico
    form_class = PoliticoForm
    template_name = 'politico_form.html'
    success_url = reverse_lazy('politico-list')


    
class PoliticoUpdateView(UpdateView):
    model = Politico
    template_name = 'politico_form.html'
    fields = ['nome', 'cpf', 'partido', 'cargo', 'email', 'telefone', 'data_nascimento']
    success_url = reverse_lazy('politico-list')


class PoliticoDeleteView(DeleteView):
    model = Politico
    template_name = 'politico_confirm_delete.html'
    success_url = reverse_lazy('politico-list')


# Partido
class PartidoListView(ListView):
    model = Partido
    template_name = 'partido_list.html'

    def get_queryset(self):
        return Partido.objects.all()
    
class PartidoCreateView(CreateView):
    model = Partido
    template_name = 'partido_form.html'
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('partido-list')


class PartidoUpdateView(UpdateView):
    model = Partido
    template_name = 'partido_form.html'
    fields = ['nome', 'sigla']
    success_url = reverse_lazy('partido-list')


class PartidoDeleteView(DeleteView):
    model = Partido
    template_name = 'partido_confirm_delete.html'
    success_url = reverse_lazy('partido-list')


# Categoria Despesa 
class CategoriaDespesaListView(ListView):
    model = CategoriaDespesa
    template_name = 'categoria_despesa_list.html'


class CategoriaDespesaCreateView(CreateView):
    model = CategoriaDespesa
    template_name = 'categoria_despesa_form.html'
    fields = ['nome']
    success_url = reverse_lazy('categoria-despesa-list')


class CategoriaDespesaUpdateView(UpdateView):
    model = CategoriaDespesa
    template_name = 'categoria_despesa_form.html'
    fields = ['nome']
    success_url = reverse_lazy('categoria-despesa-list')


class CategoriaDespesaDeleteView(DeleteView):
    model = CategoriaDespesa
    template_name = 'categoria_despesa_confirm_delete.html'
    success_url = reverse_lazy('categoria-despesa-list')


# Despesa 
class DespesaListView(ListView):
    model = Despesa
    template_name = 'despesa_list.html'


class DespesaCreateView(CreateView):
    model = Despesa
    template_name = 'despesa_form.html'
    fields = ['politico', 'categoria', 'valor', 'data', 'descricao']
    success_url = reverse_lazy('despesa-list')


class DespesaUpdateView(UpdateView):
    model = Despesa
    template_name = 'despesa_form.html'
    fields = ['politico', 'categoria', 'valor', 'data', 'descricao']
    success_url = reverse_lazy('despesa-list')


class DespesaDeleteView(DeleteView):
    model = Despesa
    template_name = 'despesa_confirm_delete.html'
    success_url = reverse_lazy('despesa-list')
'''
    
