from django.shortcuts import render

from django.views.generic import CreateView

from .models import Documento
from apps.funcionarios.models import Funcionario

class DocumentCreate(CreateView):
    model = Documento
    fields = ['descricao','arquivo']

    def post(self, request, *args, **kwargs):
        
       
        #self.object = self.get_object() # assign the object to the view
        form = self.get_form()
        
        form.instance.user_id_id = self.kwargs['funcionario_id']
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

        
       # return super().post(request, *args, **kwargs)

    # def form_valid(self, form):
    #     form.instance.user_id = 3
    #     return super().form_valid(form)
        

    # def get_queryset(self):
    #     empresa = self.request.user.funcionario.empresa
    #     return Funcionario.objects.filter(empresa=empresa)


