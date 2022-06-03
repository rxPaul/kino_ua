from django.contrib import admin
from .models import Movie, Category


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
