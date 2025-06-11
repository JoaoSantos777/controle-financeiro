from django.urls import path
from .views import relatorio_financeiro

urlpatterns = [
    path('', relatorio_financeiro, name='relatorio-financeiro'),
]