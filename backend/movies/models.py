from django.db import models


class Genre(models.Model):
    genre_id = models.IntegerField(unique=True)
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    released_date = models.DateTimeField()
    popularity = models.FloatField()
    vote_avg = models.DecimalField(max_digits=4, decimal_places=2)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title
