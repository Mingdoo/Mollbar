from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

import re
from .serializers import SignupSerializer


LOWERCASE_AND_NUMBER = re.compile('^(?=.*[a-z])(?=.*\d)[a-z\d]')
LOWERCASE_AND_UPPERCASE_AND_NUMBER = re.compile('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]')

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
    if LOWERCASE_AND_NUMBER.match(username) is None:
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

    serializer = SignupSerializer(data=request.data)

    # 1-3 / 3-1. username 고유성, 이메일 형식 유효성 확인
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data['password'])  # 비밀번호 암호화
        user.save()                                  # 유저 정보 DB에 저장

        return Response(serializer.data, status=status.HTTP_201_CREATED)
