from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import MovieCreateForm
from .mixins import ObjectListMixin
from .models import Movie, Category
from django.views.generic import View


def main(request):
    movies = Movie.objects.all()
    return render(request, 'movies/main.html', {'title': 'Home', 'movies': movies})


class MovieDetail(View):
    def get(self, request, slug):
        movie = Movie.objects.get(slug__iexact=slug)
        return render(request, 'movies/movie_detail.html', {'movie': movie})


class CategoryDetail(View):

    def get(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        movies = category.movies.all()
        context = {
            'category': category,
            'movies': movies
        }
        return render(request, 'movies/category_detail.html', context=context)


class MovieListView(ObjectListMixin, View):
    model = Movie
    template = 'movies/movie_list.html'
    multiple_str = 'movies'

    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, 'movies/movie_list.html', context={'movies': movies})


class CategoryListView(ObjectListMixin, View):
    model = Category
    template = 'movies/category_list.html'
    multiple_str = 'categories'

    # def get(self, request):
    #     categories = Category.objects.all()
    #     template = 'movies/category_list.html'
    #     return render(request, template, context={'categories': categories})


def add_movie(request):
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
        'error': form.errors
    }
    return render(request, 'movies/movie_create_form.html', context)


class MovieEdit(View):
    model = Movie
    form = MovieCreateForm
    template = 'movies/movie_edit_form.html'

    def get(self, request, slug):
        movie = Movie.objects.get(slug__iexact=slug)
        form = MovieCreateForm(instance=movie)
        return render(request, 'movies/movie_edit_form.html', context={'form': form, 'movie': movie})

    def post(self, request, slug):
        movie = Movie.objects.get(slug__iexact=slug)
        form = MovieCreateForm(request.POST, instance=movie)

        if form.is_valid():
            movie = form.save()
            return redirect(movie)
        return render(request, 'movies/movie_edit_form.html', context={'form': form, 'movie': movie})


class MovieDelete(View):
    def get(self, request, slug):
        movie = Movie.objects.get(slug__iexact=slug)
        form = MovieCreateForm(instance=movie)
        return render(request, 'movies/movie_delete_form.html', context={'movie': movie})

    def post(self, request, slug):
        movie = Movie.objects.get(slug__iexact=slug)
        movie.delete()
        return redirect(reverse('movies'))
