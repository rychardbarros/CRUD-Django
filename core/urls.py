from django.urls import path
from .views import home, save

urlpatterns = [
    path('', home), 
    path('salvar/', save, name='save'), 
]