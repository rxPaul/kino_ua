from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField('Назва', max_length=50)
    description = models.TextField('Опис')
    rating = models.IntegerField('Рейтинг')
    year = models.IntegerField('Рік')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    actors = models.CharField('Актори', max_length=50)
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
