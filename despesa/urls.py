from django.urls import path
from . import views 

urlpatterns = [
    path('', views.DespesaListView.as_view(), name='despesa-list'),
    path('criar/', views.DespesaCreateView.as_view(), name='despesa-create'),
    path('<int:pk>/editar/', views.DespesaUpdateView.as_view(), name='despesa-update'),
    path('<int:pk>/deletar/', views.DespesaDeleteView.as_view(), name='despesa-delete'),
]
