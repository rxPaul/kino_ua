from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('movie_list', views.MovieListView.as_view(), name='movies'),
    path('movie/<str:slug>/', views.MovieDetail.as_view(), name='movie'),
    path('category/', views.CategoryListView.as_view(), name='categories'),
    path('category/<str:slug>', views.CategoryDetail.as_view(), name='category'),
    path('new', views.new, name='new'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
    path('top', views.top, name='top'),
    path('add_movie', views.addMovie, name='add_movie'),
    path('update_movie/<str:slug>', views.updateMovie, name='update_movie'),

    # path('register', views, name='register'),
    # path('login', views.login, name='login')



]
