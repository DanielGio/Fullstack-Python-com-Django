from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial
    path('', views.index, name='index'),

    # Rota da página "Contatos"
    path('contato/', views.contato, name='contato'),

    # Rota da página de cadastro de Pessoa
    path('adicionar/', views.adicionar, name='adicionar'),

    # Rota para visualizar uma pessoa única pelo ID
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),

     # Rota para editar uma pessoa única pelo ID
    path('detalhes/<int:id>/editar/', views.editar, name='editar'),

    # Deletar 
    path('pessoa/<int:id>/deletar/', views.deletar, name='deletar'),
]

