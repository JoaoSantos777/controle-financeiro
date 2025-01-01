from django.http import HttpResponse
from . import views 
from django.urls import path

urlpatterns = [
    path('teste', views.test_view, name='test-view'), 

    # Politico URLs
    path('', views.PoliticoListView.as_view(), name='politico-list'),
    path('criar/', views.PoliticoCreateView.as_view(), name='politico-create'),
    path('<int:pk>/editar/', views.PoliticoUpdateView.as_view(), name='politico-update'),
    path('<int:pk>/deletar/', views.PoliticoDeleteView.as_view(), name='politico-delete'),
    path('politico/<int:pk>/', views.politico_detalhe, name='politico_detalhe'),
]