from django.urls import path,include



from .views import EmpresaCreate,EmpresaUpdate

app_name = 'empresa'


urlpatterns = [
    path('novo/',EmpresaCreate.as_view(),name='create'),
    path('editar/<int:pk>',EmpresaUpdate.as_view(),name='edit_empresa'),
   
]
