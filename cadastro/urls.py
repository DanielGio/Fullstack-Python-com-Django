from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial
    path('', views.index, name='index'),

    # Rota da página "Contatos"
    path('contato/', views.contato, name='contato')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('adicionar/', views.adicionar, name='adicionar'),
]
