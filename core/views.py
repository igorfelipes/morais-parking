from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.forms import * 
from core.models import * 


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
        return redirect('listar-veiculos')
    return render(request, 'editar-veiculo.html',{'form': form, 'veiculo': veiculo} )

def deletarVeiculo(request, id):
    veiculo = get_object_or_404(Veiculo, pk=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar-veiculos')
    return render(request, 'deletar-veiculo.html', {'veiculo': veiculo})


def entradaVeiculo(request):
    template_name = 'entrada.html'
    
    if request.method == 'POST':
        form = EntradaVeiculosForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('cadastro-ocorrencia')
    else:
        form = OcorrenciaForm()
        formContextToRender = {
            'form': form
            }
        return render(request, 'ocorrencias.html',formContextToRender)

def monitorarVagas(request):
    if request.method == 'POST':
        form = VagasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoramento-vagas')
    else:
        form = VagasForm()
        formContextToRender = {
            'form': form
        }
        return render(request, 'monitor-vagas.html', formContextToRender)

def vagasList(request):
    vagas = Vagas.objects.all() 
    return render(request, 'listar-vagas.html', {'vagas': vagas} )

def atualizarVaga(request, id):
    vagas = Vagas.objects.get(setor_type=id)
    form = VagasForm(request.POST or None, instance=vagas)
    if form.is_valid():
        form.save()
        return redirect('listar-vagas')
    return render(request, 'editar-vagas.html',{'form': form,'vagas': vagas} 
        )
