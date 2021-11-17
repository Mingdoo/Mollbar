from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer
from .models import Movie

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
