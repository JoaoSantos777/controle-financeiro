'''from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    # Politico URLs
    path('politicos/', views.PoliticoListView.as_view(), name='politico-list'),
    path('politicos/criar/', views.PoliticoCreateView.as_view(), name='politico-create'),
    path('politicos/<int:pk>/editar/', views.PoliticoUpdateView.as_view(), name='politico-update'),
    path('politicos/<int:pk>/deletar/', views.PoliticoDeleteView.as_view(), name='politico-delete'),

    # Partido
    path('partidos/', views.PartidoListView.as_view(), name='partido-list'),
    path('partidos/criar/', views.PartidoCreateView.as_view(), name='partido-create'),
    path('partidos/<int:pk>/editar/', views.PartidoUpdateView.as_view(), name='partido-update'),
    path('partidos/<int:pk>/deletar/', views.PartidoDeleteView.as_view(), name='partido-delete'),

    # CategoriaDespesa URLs
    path('categorias-despesa/', views.CategoriaDespesaListView.as_view(), name='categoria-despesa-list'),
    path('categorias-despesa/criar/', views.CategoriaDespesaCreateView.as_view(), name='categoria-despesa-create'),
    path('categorias-despesa/<int:pk>/editar/', views.CategoriaDespesaUpdateView.as_view(), name='categoria-despesa-update'),
    path('categorias-despesa/<int:pk>/deletar/', views.CategoriaDespesaDeleteView.as_view(), name='categoria-despesa-delete'),

    # Despesa URLs
    path('despesas/', views.DespesaListView.as_view(), name='despesa-list'),
    path('despesas/criar/', views.DespesaCreateView.as_view(), name='despesa-create'),
    path('despesas/<int:pk>/editar/', views.DespesaUpdateView.as_view(), name='despesa-update'),
    path('despesas/<int:pk>/deletar/', views.DespesaDeleteView.as_view(), name='despesa-delete'),
]
'''