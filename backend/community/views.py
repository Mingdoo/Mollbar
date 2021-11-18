from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ArticleSerializer
from .models import Article

from rest_framework import status
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


# READ => 인증된 사용자면 가능
# UPDATE / DELETE => 작성자 본인만 가능
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # 게시글 상세 페이지 보기 (READ)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 게시글 수정 (UPDATE)
    elif request.method == 'PUT':
        if request.user != article.user:
            return Response(
                {'message': '게시글은 작성자만 수정할 수 있습니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 게시글 삭제 (DELETE)
    else:
        if request.user != article.user:
            return Response(
                {'message': '게시글은 작성자만 삭제할 수 있습니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        article.detele()
        return Response(
            {'message': '게시글이 삭제되었습니다.'},
            status=status.HTTP_204_NO_CONTENT
        )
