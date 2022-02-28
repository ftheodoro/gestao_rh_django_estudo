from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresa.models import Empresas

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.PROTECT,default=1)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresas,on_delete=models.PROTECT,default=0)

    def __str__(self):
        return self.nome
