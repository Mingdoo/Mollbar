from django.urls import path
from . import views


urlpatterns = [
    path('genre-popular/<int:genre_id>/', views.get_popular_movies_by_genres),
    path('search/', views.search),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/ratings/', views.rate_movie),
    path('<int:movie_id>/wishlist/', views.add_wishlist),
]
