from django.urls import path,include



from .views import DepartamentosList,DepartamentoCreate,DepartamentoUpdate,DepartamentoDelete

app_name = 'departamentos'


urlpatterns = [
    path('listar/',DepartamentosList.as_view(),name='list_departamentos'),
    path('novo',DepartamentoCreate.as_view(),name='create'),
    path('update/<int:pk>',DepartamentoUpdate.as_view(),name='update_departamento'),
    path('deletar/<int:pk>',DepartamentoDelete.as_view(),name='delete_departamento'),
   
]
