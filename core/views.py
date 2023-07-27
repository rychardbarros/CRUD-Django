from django.shortcuts import render
from .models import Person

def home(request):
    person = Person.objects.all()
    return render(request, 'index.html', {'person': person})