from django.shortcuts import render
from .models import Person

def home(request):
    person = Person.objects.all()
    return render(request, 'index.html', {'person': person})

def save(request):
    name = request.POST.get('person_name')
    Person.objects.create(name=name)
    persons = Person.objects.all()
    return render(request, 'index.html', {'person': persons})