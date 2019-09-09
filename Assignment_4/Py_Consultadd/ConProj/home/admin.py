from django.contrib import admin
from .models import Example, Club, Movie, Game

# Register your models here.
admin.site.register(Example)

admin.site.register(Club)

admin.site.register(Movie)

admin.site.register(Game)
