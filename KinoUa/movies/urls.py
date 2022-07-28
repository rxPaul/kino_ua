from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('movie', views.MovieListView.as_view(), name='movies'),
    path('movie/<str:slug>/', views.MovieDetail.as_view(), name='movie_detail_url'),
    path('movie/<str:slug>/edit', views.MovieEdit.as_view(), name='movie_edit'),
    path('category/', views.CategoryListView.as_view(), name='categories'),
    path('category/<str:slug>', views.CategoryDetail.as_view(), name='category_detail_url'),
    path('add_movie', views.add_movie, name='add_movie'),

    # path('register', views, name='register'),
    # path('login', views.login, name='login')



]
