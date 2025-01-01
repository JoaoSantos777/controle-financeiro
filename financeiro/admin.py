'''from django.contrib import admin
from .models import Politico, Partido, CategoriaDespesa, Despesa

@admin.register(Politico)
class PoliticoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'partido', 'cargo', 'email', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'cpf', 'partido__nome', 'cargo', 'email')
    list_filter = ('partido', 'cargo')

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome', 'sigla')

@admin.register(CategoriaDespesa)
class CategoriaDespesaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('politico', 'categoria', 'valor', 'data', 'descricao')
    search_fields = ('politico__nome', 'categoria__nome', 'descricao')
    list_filter = ('politico', 'categoria','valor', 'data')
'''