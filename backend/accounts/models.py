from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Movie


class User(AbstractUser):
    wishlist = models.ManyToManyField(Movie, related_name="wish_users", blank=True)

    def __str__(self):
        return self.username
