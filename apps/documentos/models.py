from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse
class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    user_id = models.ForeignKey(Funcionario,on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse("funcionarios:update_funcionario", args=[self.user_id.id])
    

    def __str__(self):
        return self.descricao
