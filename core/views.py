from django.shortcuts import render, redirect
from .models import Person

def home(request):
    person = Person.objects.all()
    return render(request, 'index.html', {'person': person})

def save(request):
    name = request.POST.get('person_name')
    Person.objects.create(name=name)
    persons = Person.objects.all()
    return render(request, 'index.html', {'person': persons})

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'update.html', {'person': person})

def update(request, id):
    name = request.POST.get('person_name')
    person = Person.objects.get(id=id)
    person.name = name
    person.save()
    return redirect(home)

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(home)

def return_home(request):
    return redirect(home)
