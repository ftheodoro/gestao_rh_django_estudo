from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView

from apps.empresa.models import Empresas

class EmpresaCreate(CreateView):
    model = Empresas
    fields = ['nome']

    def form_valid(self, form):
        object = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = object
        funcionario.save()
        
        return super().form_valid(form)

class EmpresaUpdate(UpdateView):
     model = Empresas
     fields = ['nome']

