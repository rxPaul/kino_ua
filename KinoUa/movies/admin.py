from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')


admin.site.register(Movie, MovieAdmin)
