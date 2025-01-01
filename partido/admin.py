from django.contrib import admin
from .models import Partido


@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')
    search_fields = ('nome', 'sigla')
