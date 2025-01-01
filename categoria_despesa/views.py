from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CategoriaDespesa
from django.urls import reverse_lazy

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
