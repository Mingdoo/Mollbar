from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MovieSerializer
from .models import Movie, Genre
from django.db.models import F

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_id):
    # 영화 상세 정보
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_popular_movies_by_genres(request, genre_id):
    """
    해당 장르의 인기작 20편을 평균 평점 순으로 내림차순 정렬한다.
    """
    popular_movies_by_genre = (
        Movie.objects
            .filter(genres=genre_id)
            .prefetch_related('genres')
            .order_by('-vote_avg')[:20]
    )
    
    serializer = MovieSerializer(popular_movies_by_genre, many=True)

    if serializer:
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {'message': '해당 장르를 찾을 수 없습니다.'}, 
            status=status.HTTP_404_NOT_FOUND
        )
