from django.db import models
from datetime import date
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Movie(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    rating = models.IntegerField('Rating', validators=[MinValueValidator(1), MaxValueValidator(10)])
    year = models.IntegerField('Year', validators=[MinValueValidator(1900)])
    categories = models.ManyToManyField('Category')
    actors = models.ManyToManyField('Actor')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

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
    birth_date = models.DateField(null=True)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def age(self):
        today = date.today()
        born = self.birth_date
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    class Meta:
        verbose_name = 'Актор'
        verbose_name_plural = 'Актори'
        ordering = ('last_name', 'first_name')

