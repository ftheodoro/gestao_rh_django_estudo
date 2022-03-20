from django.urls import path,include
from .views import DocumentCreate


app_name = 'documentos'
urlpatterns = [
    
    path('novo/<int:funcionario_id>',DocumentCreate.as_view(),name='create_documento'),
    # path('novo',FuncionarioCreate.as_view(),name='create_funcionario'),
    # path('editar/<int:pk>',FuncionarioEdit.as_view(),name='update_funcionario'),
    # path('deletar/<int:pk>',FuncionarioDelete.as_view(),name='delete_funcionario'),
   
]
