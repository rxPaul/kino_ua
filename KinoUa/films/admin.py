from django.contrib import admin
from.models import *
# Register your models here.

class FilmsAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')


admin.site.register(Films, FilmsAdmin)
