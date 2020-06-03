from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template
from core.forms import * 
from core.models import * 

from .utils import render_to_pdf

@login_required
def home(request):
    print(type(request.user.user_type))
    return render(request, 'index.html')

def veiculosList(request):
    veiculos = Veiculo.objects.all() 
    return render(request, 'listar-veiculos.html', {'veiculos': veiculos} )

@login_required
def cadastrarVeiculo(request):
    if request.method == 'POST':
        form = CadastroVeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Veículo Cadastrado com Sucesso!')
            return redirect('index')
    else: 
        form = CadastroVeiculoForm()
        formContextToRender = {
            'form': form
            }
        return render(request, 'cadastrar-veiculo.html',formContextToRender )

def atualizarVeiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    form = CadastroVeiculoForm(request.POST or None, instance=veiculo)
    if form.is_valid():
        form.save()
        messages.info(request, 'Veículo Atualizado com Sucesso!')
        return redirect('listar-veiculos')
    return render(request, 'editar-veiculo.html',{'form': form, 'veiculo': veiculo} )

def deletarVeiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    if request.method == 'POST':
        veiculo.delete()
        messages.info(request, 'Veículo deletado com Sucesso!')
        return redirect('listar-veiculos')
    return render(request, 'deletar-veiculo.html', {'veiculo': veiculo})


def entradaVeiculo(request):
    template_name = 'entrada.html'
    
    if request.method == 'POST':
        form = EntradaVeiculosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Entrada Validada com sucesso!')
            return redirect('entrada-veiculo')
    else:
        form = EntradaVeiculosForm()
    
    context_to_render = {
        'form': form
    }
    return render(request, template_name, context_to_render)

def cadastrarEvento(request):
    if request.method == 'POST':
        form = EventosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Evento cadastrado com Sucesso!')
            return redirect('cadastro-evento')
    else:
        form = EventosForm()
        formContextToRender = {
            'form': form
            }
        return render(request, 'eventos.html',formContextToRender )

def cadastrarOcorrencia(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Ocorrência cadastrada com Sucesso! com Sucesso!')
            return redirect('cadastro-ocorrencia')
    else:
        form = OcorrenciaForm()

    formContextToRender = {
        'form': form
        }
    return render(request, 'ocorrencias.html',formContextToRender)

def vagasList(request):
    vagas = Vagas.objects.all() 
    return render(request, 'listar-vagas.html', {'vagas': vagas} )

def atualizarVaga(request, id):
    vagas = Vagas.objects.get(setor_type=id)
    form = VagasForm(request.POST or None, instance=vagas)
    if form.is_valid():
        form.save()
        messages.info(request, 'Vaga atualizada com Sucesso!')
        return redirect('listar-vagas')
    return render(request, 'editar-vagas.html',{'form': form,'vagas': vagas} 
        )

def gerarRelatorio_index(request):
    return render(request, 'gerar-relatorio-index.html')

def gerarRelatorio(request):
    messages.info(request, 'Relatório gerado com sucesso!')

    vagas = Vagas.objects.all()
    ocorrencias = Ocorrencia.objects.all()

    template = get_template('utils/base-pdf.html')
    
    context = {
        'vagas': vagas,
        'username': request.user,
        'ocorrencias': ocorrencias,
    }
    
    html = template.render(context)
    pdf = render_to_pdf('utils/base-pdf.html', context)
    
    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponse('Not found')