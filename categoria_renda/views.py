from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CategoriaRenda
from django.urls import reverse_lazy

# Categoria Renda 
class CategoriaRendaListView(ListView):
    model = CategoriaRenda
    template_name = 'categoria_renda_list.html'


class CategoriaRendaCreateView(CreateView):
    model = CategoriaRenda
    template_name = 'categoria_renda_form.html'
    fields = ['nome']
    success_url = reverse_lazy('categoria-renda-list')


class CategoriaRendaUpdateView(UpdateView):
    model = CategoriaRenda
    template_name = 'categoria_renda_form.html'
    fields = ['nome']
    success_url = reverse_lazy('categoria-renda-list')


class CategoriaRendaDeleteView(DeleteView):
    model = CategoriaRenda
    template_name = 'categoria_renda_confirm_delete.html'
    success_url = reverse_lazy('categoria-renda-list')
