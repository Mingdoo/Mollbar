from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, MovieDetailSerializer, RatingSerializer
from .models import Movie, Rating

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_id):
    """
    영화 상세 정보 및 해당 영화의 평점/리뷰 목록을 보여준다.
    """
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = MovieDetailSerializer(movie)
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


@api_view(['POST', 'DELETE'])
def rate_movie(request, movie_id):
    """
    영화에 대한 평가를 등록/수정/삭제한다.
    """
    movie = get_object_or_404(Movie, movie_id=movie_id)
    rating = movie.ratings.filter(user=request.user).first()

    if request.method == 'POST':
        # 해당 영화에 대한 평가가 없는 경우 => 평가 등록 (CREATE)
        if not rating:
            serializer = RatingSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 해당 영화에 대한 평가가 있는 경우 => 평가 수정 (UPDATE)
        else:
            serializer = RatingSerializer(rating, data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 평가 삭제 (DELETE)
    else:
        if rating:
            rating.delete()
            return Response(
                {'message': '평가가 삭제되었습니다.'},
                status=status.HTTP_204_NO_CONTENT
            )
