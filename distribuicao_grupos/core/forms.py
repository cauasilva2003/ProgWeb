from django import forms
from .models import Aluno, Tema

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula']

class TemaForm(forms.ModelForm):
    data_apresentacao = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    horario_inicio = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
    horario_fim = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )

    class Meta:
        model = Tema
        fields = ['titulo', 'quantidade_grupos', 'alunos_por_grupo', 'data_apresentacao', 'horario_inicio', 'horario_fim']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_grupos': forms.NumberInput(attrs={'class': 'form-control'}),
            'alunos_por_grupo': forms.NumberInput(attrs={'class': 'form-control'}),
        }


