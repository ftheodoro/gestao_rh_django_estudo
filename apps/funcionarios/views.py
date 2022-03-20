from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from .models import Funcionario




class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:list_funcionarios')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
       
       
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionarioSplit = funcionario.nome.split(' ')
        username = "{}{}".format(funcionarioSplit[0],funcionarioSplit[1])
        
      
        funcionario.user = User.objects.create(
             username= username
            
             )
        funcionario.save()
        return super(FuncionarioCreate,self).form_valid(form)



    





