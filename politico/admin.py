from django.contrib import admin
from .models import Politico

@admin.register(Politico)
class PoliticoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'partido', 'cargo', 'email', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'cpf', 'partido__nome', 'cargo', 'email')
    list_filter = ('partido', 'cargo')
