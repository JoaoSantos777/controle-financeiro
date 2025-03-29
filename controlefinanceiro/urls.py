from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('partido/', include('partido.urls')),
    path('politico/', include('politico.urls')),
    path('despesa/', include('despesa.urls')),
    path('categoria-despesa/', include('categoria_despesa.urls')),
    path('categoria-renda/', include('categoria_renda.urls')),
    path('renda/', include('renda.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('accounts/', include('accounts.urls')),
]
