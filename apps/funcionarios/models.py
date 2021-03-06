
from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresa.models import Empresas
from django.urls import reverse
from django.db.models import Sum


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT, default=1)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresas, on_delete=models.PROTECT, default=0, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("funcionarios:list_funcionarios")

    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.all().aggregate(Sum('horas'))[
            'horas__sum']
        return total

    def __str__(self):
        return self.nome
