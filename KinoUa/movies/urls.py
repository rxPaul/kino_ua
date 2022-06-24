from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('movie/<int:post_id>/', showMovie, name='movie'),
    path('categories/', categories, name='categories'),
    path('new', new, name='new'),
    path('coming_soon', coming_soon, name='coming_soon'),
    path('top', top, name='top'),
    path('add_movie', addMovie, name='add_movie'),
    path('update_movie/<str:pk>', updateMovie, name='update_movie'),

    # path('register', views, name='register'),
    # path('login', views.login, name='login')



]
