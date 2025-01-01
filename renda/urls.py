from django.urls import path
from .views import RendaListView, RendaCreateView, RendaUpdateView, RendaDeleteView

urlpatterns = [
    path('', RendaListView.as_view(), name='renda-list'),
    path('adicionar/', RendaCreateView.as_view(), name='renda-create'),
    path('editar/<int:pk>/', RendaUpdateView.as_view(), name='renda-update'),
    path('excluir/<int:pk>/', RendaDeleteView.as_view(), name='renda-delete'),
]
