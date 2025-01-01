from django.urls import path
from . import views 

urlpatterns = [
    # Partido URLs
    path('', views.PartidoListView.as_view(), name='partido-list'),
    path('criar/', views.PartidoCreateView.as_view(), name='partido-create'),
    path('<int:pk>/editar/', views.PartidoUpdateView.as_view(), name='partido-update'),
    path('<int:pk>/deletar/', views.PartidoDeleteView.as_view(), name='partido-delete'),

]
