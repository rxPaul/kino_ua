from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('categories', views.categories, name='categories'),
    path('new', views.new, name='new'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
    path('top', views.top, name='top'),
    path('add', views.add, name='add'),
    path('actors', views.actor_view, name='actors'),
    path('actor/<int:id>', views.actor_from_id, name='actor'),
]
