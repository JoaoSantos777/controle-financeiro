from django.contrib import admin
from .models import CategoriaRenda

@admin.register(CategoriaRenda)
class CategoriaRendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
