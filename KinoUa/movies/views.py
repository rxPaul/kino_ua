from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .forms import MovieCreateForm
from .models import Movie, Actor


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'title': 'Головна', 'movies': movies})


def categories(request):
    return render(request, 'movies/categories.html')


def new(request):
    return render(request, 'movies/new.html')


def top(request):
    return render(request, 'movies/top.html')


def coming_soon(request):
    return render(request, 'movies/coming_soon.html')

def add(request):
    if request.method == 'GET':
        form = MovieCreateForm()
        return render(request, 'movies/add.html', {'form': form, 'error': ''})

    form = MovieCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'movies/add.html', {'form': form, 'error': 'Невірна форма'})

def actor_view(request):
    actors = Actor.objects.all()
    return render(request, 'movies/actors.html', {'actors': actors})

def actor_from_id(request, id):
    if Actor.objects.filter(pk=id).exists():
        actor = Actor.objects.get(pk=id)
        return render(request, 'movies/actor.html', {'actor': actor})
    return redirect('/')
    
