from django.urls import path
from .views import home, save, update, edit, delete, return_home

urlpatterns = [
    path('', home), 
    path('salvar/', save, name='save'),
    path('editar/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('deletar/<int:id>', delete, name='delete'),
    path('return_home/', return_home, name='back'),

]