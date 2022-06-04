from django.contrib import admin
from .models import Movie, Category, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)
