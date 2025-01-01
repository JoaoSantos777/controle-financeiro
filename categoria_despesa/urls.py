from django.urls import path
from . import views 

urlpatterns = [
    # CategoriaDespesa URLs
    path('', views.CategoriaDespesaListView.as_view(), name='categoria-despesa-list'),
    path('criar/', views.CategoriaDespesaCreateView.as_view(), name='categoria-despesa-create'),
    path('<int:pk>/editar/', views.CategoriaDespesaUpdateView.as_view(), name='categoria-despesa-update'),
    path('<int:pk>/deletar/', views.CategoriaDespesaDeleteView.as_view(), name='categoria-despesa-delete'),
]
