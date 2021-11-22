from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment, Kmovie
import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def article_list(request):
    # 게시글 전체 목록 보기 (READ)
    # TODO: pagination 추가하기
    if request.method == 'GET':
        articles = Article.objects.all()
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
        
        article.delete()
        return Response(
            {'message': '게시글이 삭제되었습니다.'},
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET', 'POST'])
def comment_list(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # 게시글의 댓글 목록 보기 (READ)
    if request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # 게시글에 새 댓글 작성하기 (CREATE)
    else:
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, comment_user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.comment_user:
        return Response(
            {'message': '댓글은 작성자만 수정/삭제할 수 있습니다.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # 댓글 수정하기 (UPDATE)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 댓글 삭제하기 (DELETE)
    else:
        comment.delete()
        return Response(
            {'message': '댓글이 삭제되었습니다.'},
            status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET'])
def get_korean_movies(request):
    """
    10개의 사지선다 한국영화 퀴즈 set를 만든다.

    [응답 데이터 형태]

    [
        {
            "poster_path": "/adfasdfssdfsdasdfsdfasdf.jpg",
            "options": [
                { "title": "승리호", "isCorrect": false },
                { "title": "반도", "isCorrect": false },
                { "title": "기생충", "isCorrect": true },
                { "title": "부산행", "isCorrect": false },
            ]
        },
    ]
    """
    # model에서 ordering = ['?'] 조건을 주었으므로, 요청 시마다 랜덤 정렬된 queryset이 넘어온다.
    kmovies = Kmovie.objects.all()[:40]
    quiz_set = []

    for i in range(0, 40, 4):
        movie1 = kmovies[i]
        movie2 = kmovies[i + 1]
        movie3 = kmovies[i + 2]
        movie4 = kmovies[i + 3]

        quiz_data = {
            "poster_path": movie1.poster_path,
            "options": [
                { "title": movie1.title, "isCorrect": True },
                { "title": movie2.title, "isCorrect": False },
                { "title": movie3.title, "isCorrect": False },
                { "title": movie4.title, "isCorrect": False },
            ]
        }

        random.shuffle(quiz_data["options"])
        quiz_set.append(quiz_data)

    return Response(data=quiz_set)
