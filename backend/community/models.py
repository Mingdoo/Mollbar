from django.db import models
from django.conf import settings


class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(null=True, max_length=50)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return self.article_title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(null=True, max_length=50)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        return self.content


class Kmovie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    vote_count = models.IntegerField()
    poster_path = models.CharField(max_length=200)

    class Meta:
        ordering = ['?']  # 랜덤 정렬

    def __str__(self):
        return self.title
        