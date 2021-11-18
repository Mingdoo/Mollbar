from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.validators import (
    MinValueValidator, MaxValueValidator
)
from movies.models import Movie


class User(AbstractUser):
    ratings = models.ManyToManyField(Movie, through='Rating')


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_movie_rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.user_movie_rate
