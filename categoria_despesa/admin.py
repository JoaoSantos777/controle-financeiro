from django.contrib import admin
from .models import CategoriaDespesa

@admin.register(CategoriaDespesa)
class CategoriaDespesaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
