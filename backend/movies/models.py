from django.db import models
from django.conf import settings
from django.core.validators import (
    MinValueValidator, MaxValueValidator
)


class Genre(models.Model):
    genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.DecimalField(max_digits=4, decimal_places=2)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    video_url = models.CharField(max_length=20, null=True)
    actors = models.JSONField()
    director = models.CharField(max_length=100)

    class Meta:
        ordering = ['-popularity', ]

    def __str__(self):
        return self.title


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(null=True, max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField(null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.user}: {self.rate} / 10'
