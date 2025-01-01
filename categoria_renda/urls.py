from django.urls import path
from .views import (
    CategoriaRendaListView, 
    CategoriaRendaCreateView, 
    CategoriaRendaUpdateView, 
    CategoriaRendaDeleteView
)

urlpatterns = [
    path('', CategoriaRendaListView.as_view(), name='categoria-renda-list'),
    path('adicionar/', CategoriaRendaCreateView.as_view(), name='categoria-renda-create'),
    path('editar/<int:pk>/', CategoriaRendaUpdateView.as_view(), name='categoria-renda-update'),
    path('excluir/<int:pk>/', CategoriaRendaDeleteView.as_view(), name='categoria-renda-delete'),
]
