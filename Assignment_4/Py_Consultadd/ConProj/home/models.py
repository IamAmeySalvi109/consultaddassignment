from django.db import models

# Create your models here.

class Example(models.Model):
    name = models.CharField(max_length = 50, unique = False)
    age = models.IntegerField()
    number = models.IntegerField()

    def __int__(self):
        return self.number

    class Meta:
        verbose_name_plural = "Example"


class Club(models.Model):
    name = models.CharField(max_length = 50, unique = False)
    country = models.CharField(max_length = 50)
    trophies = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Football Club"


class Movie(models.Model):
    movie = models.CharField(max_length = 50, unique = False)
    director = models.CharField(max_length = 50, unique = False)
    year = models.IntegerField()

    def __str__(self):
        return self.movie

    class Meta:
        verbose_name_plural = "Film"


class Game(models.Model):
    game = models.CharField(max_length = 50, unique = False)
    publisher = models.CharField(max_length = 50, unique = False)
    rating = models.IntegerField()

    def __str__(self):
        return self.publisher

    class Meta:
        verbose_name_plural = "Game"