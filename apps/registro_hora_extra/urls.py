from django.urls import path, include
from .views import HoraExtraList, HoraExtraEdit, DeleteExtra, CreateHoraExtra


app_name = 'registro_hora_extra'
urlpatterns = [

    path('', HoraExtraList.as_view(), name='list_horaextra'),
    path('novo', CreateHoraExtra.as_view(), name='create_horaextra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='edit_hora_extra'),
    path('delete/<int:pk>', DeleteExtra.as_view(), name='delete_hora_extra'),


]
