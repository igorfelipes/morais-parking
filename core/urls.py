from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name="index"),
    path('listar-veiculos/', veiculosList, name="listar-veiculos"),
    path('cadastrar-veiculo/', cadastrarVeiculo, name='cadastrar-veiculo'),
    path('editar-veiculo/<int:id>/', atualizarVeiculo, name='editar-veiculo'),
    path('deletar-veiculo/<int:id>/', deletarVeiculo, name='deletar-veiculo'),
    path('entrada/', entradaVeiculo, name='entrada-veiculo'),
    path('eventos/', cadastrarEvento, name='cadastro-evento'),
    path('ocorrencia/', cadastrarOcorrencia, name='cadastro-ocorrencia'),
    path('listar-vagas/', vagasList, name='listar-vagas'),
    path('editar-vagas/<int:id>/', atualizarVaga, name='atualizar-vagas'),
    path('gerar-relatorio-index/', gerarRelatorio_index, name='gerar-relatorio-index'),
    path('gerar-relatorio/', gerarRelatorio, name='gerar-relatorio'),
]
