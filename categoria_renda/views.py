from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CategoriaRenda
from django.urls import reverse_lazy

# Categoria Renda 
class CategoriaRendaListView(ListView):
    model = CategoriaRenda
    template_name = 'categoria_renda_list.html'

    def get_queryset(self):
        return CategoriaRenda.objects.filter(user=self.request.user)


class CategoriaRendaCreateView(CreateView):
    model = CategoriaRenda
    template_name = 'categoria_renda_form.html'
    fields = ['nome']
    success_url = reverse_lazy('categoria-renda-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoriaRendaUpdateView(UpdateView):
    model = CategoriaRenda
    template_name = 'categoria_renda_form.html'
    fields = ['nome']
    success_url = reverse_lazy('categoria-renda-list')

    def get_queryset(self):
        return CategoriaRenda.objects.filter(user=self.request.user)


class CategoriaRendaDeleteView(DeleteView):
    model = CategoriaRenda
    template_name = 'categoria_renda_confirm_delete.html'
    success_url = reverse_lazy('categoria-renda-list')

    def get_queryset(self):
        return CategoriaRenda.objects.filter(user=self.request.user)
