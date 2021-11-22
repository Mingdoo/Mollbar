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
                serializer.save(user=request.user, username=request.user.username, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # 해당 영화에 대한 평가가 있는 경우 => 평가 수정 (UPDATE)
        else:
            serializer = RatingSerializer(rating, data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, username=request.user.username, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # 평가 삭제 (DELETE)
    else:
        if rating:
            rating.delete()
            return Response(
                {'message': '평가가 삭제되었습니다.'},
                status=status.HTTP_204_NO_CONTENT
            )


@api_view(['GET'])
@permission_classes([AllowAny])
def search(request):
    """
    [request 예시]
    GET '{{BASE_URL}}/api/v1/movies/search/'

    data: {
        "query": "토이",
        "genre": 16,
        "min_rate": 7.8,
    }

    [response 예시]
    [
        {
            "id": 862,
            "title": "토이 스토리",
            "released_date": "1995-10-30",
            ...
        },
    ]
    """
    search_word = request.data.get('query', '').strip()
    genre = request.data.get('genre', '')
    min_rate = request.data.get('min_rate', 0)

    # 1. 검색어 필터링
    if search_word:
        movies = Movie.objects.filter(title__icontains=search_word)
    else:
        movies = Movie.objects.all()
    
    # 2. 장르 필터링
    if genre:
        movies = movies.filter(genres=genre)
        
    # 3. 유저 평점 필터링
    if min_rate:
        movies = movies.filter(vote_avg__gte=min_rate)

    if not movies:
        return Response(
            {"message": "조건을 만족하는 영화가 없습니다."},
            status=status.HTTP_204_NO_CONTENT
        )

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_wishlist(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)

    if movie in request.user.wishlist.all():
        request.user.wishlist.remove(movie)
        print('remove')
        return Response(status=status.HTTP_200_OK)
    else:
        request.user.wishlist.add(movie)
        print('add')
        return Response(status=status.HTTP_200_OK)
