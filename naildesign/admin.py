from django.contrib import admin
from .models import Agendamento, Servico, Modalidade, Profissional

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servico', 'data_horario')  # Atualize aqui
    list_filter = ('data_horario',)  # Atualize aqui
    search_fields = ('usuario__username', 'servico__nome')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'modalidade', 'preco')
    list_filter = ('modalidade',)
    search_fields = ('nome', 'modalidade__nome')

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Atualize aqui com os campos desejados
    search_fields = ('nome',)  # Adapte conforme o que deseja pesquisar