from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    rating = models.IntegerField('Rating')
    year = models.IntegerField('Age')
    categories = models.ManyToManyField('Category')
    actors = models.ManyToManyField('Actor')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    # image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
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
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'
        ordering = ('last_name', 'first_name')


'''class Rating(models.Model):
    movie =
    value =
    user =
    date_created ='''
