from django.db import models
from django.urls  import reverse
from apps.empresa.models import Empresas
class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    empresa = models.ForeignKey(Empresas,on_delete=models.PROTECT)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('departamentos:list_departamentos')
    
