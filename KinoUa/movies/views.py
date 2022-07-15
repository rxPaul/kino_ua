from django.shortcuts import render, redirect
from .forms import MovieCreateForm
from .models import Movie, Category
from django.views.generic import View

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'title': 'Home', 'movies': movies})


class MovieDetail(View):
    def get(self, request, slug):
        movie = Movie.objects.get(slug__iexact=slug)
        return render(request, 'movies/movie.html', {'movie': movie})


class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        template = 'movies/movie_list.html'
        return render(request, template, context={'movies': movies})

class CategoryListView(View):

    def get(self, request):
        categories = Category.objects.all()
        template = 'movies/category_list.html'
        return render(request, template, context={'categories': categories})


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


def updateMovie(request, id):
    obj = Movie.objects.get(id)
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
