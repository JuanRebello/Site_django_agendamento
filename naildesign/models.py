from django.db import models
from django.contrib.auth.models import User

class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, related_name="servicos")
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidades = models.ManyToManyField(Servico, related_name="profissionais")

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_horario = models.DateTimeField()

    class Meta:
        unique_together = ('profissional', 'data_horario')  # Garante que o mesmo horário não seja agendado para o mesmo profissional.

    def __str__(self):
        return f"{self.usuario.username} - {self.servico.nome} com {self.profissional.nome} em {self.data_horario.strftime('%d/%m/%Y %H:%M')}"
