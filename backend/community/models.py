from django.db import models
from django.conf import settings
from movies.models import Movie


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    is_review = models.BooleanField()
    article_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return self.article_title
