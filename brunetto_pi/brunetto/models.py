from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Cargo(BaseModel):
    nome = models.CharField(max_length=100)


class Colaborador(BaseModel):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField(unique=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='colaboradores')


class Massa(BaseModel):
    nome = models.CharField(max_length=100)

class RegistroDiarioProducao(BaseModel):
    autor = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='autor_registros')
    lider_producao = models.ForeignKey(Colaborador, on_delete=models.CASCADE, related_name='lider_registros')
    data = models.DateField()
    produto_acabado_massas = models.ForeignKey(Massa, on_delete=models.CASCADE, related_name='massa_acabadas')
