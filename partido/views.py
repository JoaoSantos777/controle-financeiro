from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Partido
from django.urls import reverse_lazy

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
