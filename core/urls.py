from django.urls import path
from .views import home, save, update, edit, delete

urlpatterns = [
    path('', home), 
    path('salvar/', save, name='save'),
    path('editar/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('deletar/<int:id>', delete, name='delete'),

]