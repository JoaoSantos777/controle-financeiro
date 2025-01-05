from django.contrib import admin
from .models import Renda

@admin.register(Renda)
class RendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'valor', 'valor_disponivel', 'data_recebimento')
    search_fields = ('nome', 'categoria__nome')
