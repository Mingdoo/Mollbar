from django.shortcuts import get_list_or_404
from .serializers import ArticleSerializer
from .models import Article

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def article_list(request):
    # 게시글 전체 목록 보기 (READ)
    # TODO: pagination 추가하기
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleSerializer(articles, many=True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    # 게시글 생성 (CREATE)
    else:
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
