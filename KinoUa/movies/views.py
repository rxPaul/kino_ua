from django.shortcuts import render, redirect
from .forms import MovieCreateForm
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'title': 'Home', 'movies': movies})

def showMovie(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie.html', {'title': 'title', 'movies': movies})

def categories(request):
    return render(request, 'movies/categories.html')


def new(request):
    return render(request, 'movies/new.html')


def top(request):
    return render(request, 'movies/top.html')


def coming_soon(request):
    return render(request, 'movies/coming_soon.html')


def addMovie(request):
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


def updateMovie(request, pk):
    obj = Movie.objects.get(pk)
    form = MovieCreateForm(instance=obj)
    context = {'form': form}
    return render(request, 'movies/add.html', context)
#
# def login(request):
#     pass
#
#
# class SignUp(CreateView):
#     form_class = UserCreationForm()
#     success_url = reverse_lazy('login')
