from django import forms
from django.forms import ModelForm
from core.models import Veiculo, Entrada, Evento, Ocorrencia


class CadastroVeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'proprietario', 'matricula', 'curso', 'area_especial']


class EntradaVeiculosForm(ModelForm):

    placa = forms.CharField(max_length=7)

    def clean_placa(self):
        placaInput = self.cleaned_data['placa']

        placa = Veiculo.objects.filter(placa=placaInput)

        if not placa:
            print(placa)
            raise forms.ValidationError( 'Placa não cadastrada ')
        
        return placaInput


    class Meta:
        model = Entrada
        fields = ['setor_type', 'placa']

class EventosForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['evento', 'data', 'setor_type', 'descrição']

class OcorrenciaForm(ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['placa','setor_type','occurrence_type','obs']
    