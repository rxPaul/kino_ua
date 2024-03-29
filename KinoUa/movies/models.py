from django.db import models
from datetime import date


# Create your models here.
class Movie(models.Model):
    title = models.CharField('Назва', max_length=50)
    description = models.TextField('Опис')
    rating = models.IntegerField('Рейтинг')
    year = models.IntegerField('Рік')
    categories = models.ManyToManyField('Category')
    actors = models.ManyToManyField('Actor')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
        ordering = ('time_create', 'title')


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField()
    birth_date = models.DateField(max_length=8, null=True)
    nationality = models.CharField(max_length=50)



    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Актор'
        verbose_name_plural = 'Актори'
        ordering = ('last_name', 'first_name')



class ActorNew(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(max_length=8, null=True)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name


    class Meta:
        verbose_name = 'Актор'
        verbose_name_plural = 'Актори'
        ordering = ('first_name', 'last_name')

