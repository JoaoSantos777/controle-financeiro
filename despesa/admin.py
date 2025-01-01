from django.contrib import admin
from .models import Despesa


@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('politico', 'categoria', 'valor', 'data', 'descricao')
    search_fields = ('politico__nome', 'categoria__nome', 'descricao')
    list_filter = ('politico', 'categoria','valor', 'data')
