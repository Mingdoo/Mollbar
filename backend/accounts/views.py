from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
import re

from .serializers import UserSerializer, ProfileSerializer


LOWERCASE_OR_NUMBER = re.compile('^([a-z0-9])')
LOWERCASE_AND_UPPERCASE_AND_NUMBER = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]')

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # request: (username, password, password_confirmation, email)
    username = request.data['username']
    password = request.data['password']
    password_confirmation = request.data['passwordConfirmation']

    # 1-1. username 글자수 확인
    if not (6 <= len(username) <= 50):
        return Response(
            {'username': '아이디는 6글자 이상 50글자 이하여야 합니다.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # 1-2. username이 소문자 및 숫자로 이루어졌는지 확인
    if LOWERCASE_OR_NUMBER.match(username) is None:
        return Response(
            {'username': '아이디는 소문자 및 숫자로 이루어져야 합니다.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # 2-1. 비밀번호 일치 여부 확인
    if password != password_confirmation:
        return Response(
            {'password': '비밀번호가 일치하지 않습니다.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # 2-2. 비밀번호 글자수 확인
    if not (6 <= len(password) <= 50):
        return Response(
            {'password': '비밀번호는 6글자 이상 50글자 이하여야 합니다.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # 2-3. 비밀번호가 대문자, 소문자 및 숫자로 이루어졌는지 확인
    if LOWERCASE_AND_UPPERCASE_AND_NUMBER.match(password) is None:
        return Response(
            {'username': '비밀번호는 소문자, 대문자 및 숫자로 이루어져야 합니다.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    serializer = UserSerializer(data=request.data)

    # 1-3 / 3-1. username 고유성, 이메일 형식 유효성 확인
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data['password'])  # 비밀번호 암호화
        user.save()                                  # 유저 정보 DB에 저장

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def change_password(request):
    # request: (newPwd, newPwdConfirmation)
    new_password = request.data['newPwd']
    new_password_confirmation = request.data['newPwdConfirmation']

    # 1. 비밀번호 글자수 확인
    if not (6 <= len(new_password) <= 50):
        return Response(
            {'new_password': '새 비밀번호는 6글자 이상 50글자 이하여야 합니다.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    # 2. 비밀번호가 대문자, 소문자 및 숫자로 이루어졌는지 확인
    if LOWERCASE_AND_UPPERCASE_AND_NUMBER.match(new_password) is None:
        return Response(
            {'new_password': '새 비밀번호는 소문자, 대문자 및 숫자로 이루어져야 합니다.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    # 3. 비밀번호 일치 여부 확인
    if new_password != new_password_confirmation:
        return Response(
            {'new_password': '비밀번호가 일치하지 않습니다.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user_data = {
        'username': request.user.username,
        'password': new_password,
        'email': request.user.email,
    }
    
    serializer = UserSerializer(request.user, data=user_data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(new_password)  # 비밀번호 암호화
        user.save()                      # 유저 정보 DB에 저장

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def profile(request, user_id):
    # user_id를 받아서 해당 유저의 정보를 리턴한다.
    user = get_object_or_404(get_user_model(), id=user_id)

    serializer = ProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
