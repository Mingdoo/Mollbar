from django.db import models
from django.conf import settings
from movies.models import Movie


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return self.article_title
