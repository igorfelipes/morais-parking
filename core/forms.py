from django import forms
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from core.models import Veiculo, Entrada, Evento, Ocorrencia, Vagas


class CadastroVeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'proprietario', 'matricula', 'curso', 'area_especial']


class EntradaVeiculosForm(ModelForm):

    placa = forms.CharField(max_length=7)

    def clean_placa(self):
        placaInput = self.cleaned_data['placa']

        placa = Veiculo.objects.filter(placa=placaInput)

        setor_type = self.cleaned_data['setor_type']

        if not placa:
            raise forms.ValidationError( 'Placa não cadastrada ')

       
        placa = Veiculo.objects.get(placa=placaInput)
        vaga = Vagas.objects.get(setor_type=setor_type)

        if placa.area_especial:
            vaga.vagas_especiais_ocupadas += 1 
        else:
            vaga.vagas_normais_ocupadas +=1

        vaga.save()
        return placaInput


    class Meta:
        model = Entrada
        fields = ['setor_type', 'placa']

class EventosForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['evento', 'data', 'setor_type', 'descrição']

class OcorrenciaForm(ModelForm):
    placa = forms.CharField(max_length=7)

    def clean_placa(self):
        placaInput = self.cleaned_data['placa']

        placa = Veiculo.objects.filter(placa=placaInput)

        if not placa:
            raise forms.ValidationError( 'Placa não cadastrada ')

        return placaInput


    class Meta:
        model = Ocorrencia
        fields = ['placa','setor_type','occurrence_type','obs']

class VagasForm(ModelForm):
    class Meta:
        model = Vagas
        fields = ['vagas_normais', 'vagas_especiais','setor_type', 'vagas_normais_ocupadas', 'vagas_especiais_ocupadas']
    