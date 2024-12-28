from django import forms
from django.core.exceptions import ValidationError
from .models import Profissional, Servico, Agendamento
from django.utils import timezone

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['profissional', 'servico', 'data_horario']  # Campos que aparecerão no formulário
        widgets = {
            'data_horario': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Widget para data e hora
        }

    def clean_data_horario(self):
        data_horario = self.cleaned_data.get('data_horario')
        
        # Verificar se a data é no futuro
        if data_horario <= timezone.now():
            raise ValidationError("A data e hora devem ser no futuro.")
        
        # Verificar se o horário já foi agendado para o profissional
        profissional = self.cleaned_data.get('profissional')
        if Agendamento.objects.filter(data_horario=data_horario, profissional=profissional).exists():
            raise ValidationError("Esse horário já foi agendado para esse profissional.")
        
        return data_horario
