from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_id>/', views.movie_detail),
    path('genre-popular/<int:genre_id>/', views.get_popular_movies_by_genres),
]
