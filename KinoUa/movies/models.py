from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse
from django.utils.text import slugify

def gen_slug(s):
    return slugify(s, allow_unicode=True)

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    movies = models.ManyToManyField('Movie', verbose_name='Movie')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Movie(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description')
    rating = models.FloatField('Rating', validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True)
    year = models.IntegerField('Age')
    categories = models.ManyToManyField('Category', verbose_name='Category')
    actors = models.ManyToManyField('Actor')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    movie_poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-time_create']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.slug})





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
