from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import AddForm
from .models import Films


# Create your views here.
def index(request):
    film_s = Films.objects.all()
    return render(request, 'films/index.html', {'title': 'Головна', 'films': film_s})


def categories(request):
    return render(request, 'films/categories.html')


def new(request):
    return render(request, 'films/new.html')


def top(request):
    return render(request, 'films/top.html')


def coming_soon(request):
    return render(request, 'films/coming_soon.html')

def add(request):
    error = ''
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = ('Невірна форма')
    form = AddForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'films/add.html', context)
