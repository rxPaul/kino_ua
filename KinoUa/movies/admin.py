from django.contrib import admin
from .models import Movie, Category, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)
