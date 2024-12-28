from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Profissional, Servico, Agendamento
from .forms import AgendamentoForm

# Página inicial
def inicio(request):
    return render(request, 'design/inicio.html')

# Página de serviços
def servicos(request):
    return render(request, 'design/servicos.html')

# Página do espaço
def espaco(request):
    return render(request, 'design/espaco.html')

# Página de agendamento
# Página de agendamento
@login_required
def agendar_horario(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        
        # Verificar se o formulário é válido
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user  # Associar o usuário logado ao agendamento
            agendamento.save()  # Salvar o agendamento
            return JsonResponse({'success': True, 'message': 'Agendamento realizado com sucesso!'})
        else:
            # Retornar erros de validação do formulário
            return JsonResponse({'success': False, 'message': form.errors})
    
    # Carregar profissionais e serviços para o modal
    profissionais = Profissional.objects.all()
    servicos = Servico.objects.all()

    # Buscar os agendamentos do usuário logado
    agendamentos = Agendamento.objects.filter(usuario=request.user)

    form = AgendamentoForm()  # Instanciar o formulário

    return render(request, 'design/agendamento.html', {
        'profissionais': profissionais,
        'servicos': servicos,
        'agendamentos': agendamentos,  # Passando os agendamentos filtrados para o template
        'form': form,  # Passando o formulário para o template
    })
