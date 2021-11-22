from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list),
    path('<int:article_id>/', views.article_detail),
    path('<int:article_id>/comments/', views.comment_list),
    path('<int:article_id>/comments/<int:comment_id>/', views.comment_update_or_delete),
    path('kmovie_quiz/', views.get_korean_movies),
]
