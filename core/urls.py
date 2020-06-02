from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name="index"),
    path('listar-veiculos/', veiculosList, name="listar-veiculos"),
    path('cadastrar-veiculo/', cadastrarVeiculo, name='cadastrar-veiculo'),
    path('editar-veiculo/<int:id>/', atualizarVeiculo, name='editar-veiculo'),
    path('deletar-veiculo/<int:id>/', deletarVeiculo, name='deletar-veiculo'),
    path('entrada/', entradaVeiculo, name='entrada-veiculo'),
]
