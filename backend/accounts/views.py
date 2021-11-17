from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import SignupSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # request: (username, password, email)
    user_info = request.data

    # front: 글자수 / password 일치 여부 검사
    # back: username 고유성 / 이메일 주소 유효성 검사
    serializer = SignupSerializer(data=user_info)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(user_info['password'])  # 비밀번호 암호화
        user.save()                               # 유저 정보 DB에 저장

        return Response(serializer.data, status=status.HTTP_201_CREATED)
