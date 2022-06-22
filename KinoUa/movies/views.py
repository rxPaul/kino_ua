from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import MovieCreateForm
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'title': 'Home', 'movies': movies})


def categories(request):
    return render(request, 'movies/categories.html')


def new(request):
    return render(request, 'movies/new.html')


def top(request):
    return render(request, 'movies/top.html')


def coming_soon(request):
    return render(request, 'movies/coming_soon.html')

def add(request):
    error = ''
    if request.method == 'POST':
        form = MovieCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = ('Wrong form')
    form = MovieCreateForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'movies/add.html', context)

# def login(request):
#     pass


# class SignUp(CreateView):
#     form_class = UserCreationForm()
#     success_url = reverse_lazy('login')
