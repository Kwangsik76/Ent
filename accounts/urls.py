from django.urls import path, include

urlpatterns = [
    # 로그인과 관련된 URL 패턴
    path('', include('dj_rest_auth.urls')),
    # - password/reset/: 비밀번호 재설정 요청
    # - password/reset/confirm/: 비밀번호 재설정 확인
    # - login/: 로그인
    # - logout/: 로그아웃
    # - user/: 현재 사용자 정보
    # - password/change/: 비밀번호 변경
    path('signup/', include('dj_rest_auth.registration.urls')),
    # 회원 가입과 관련된 URL 패턴
    # - signup/: 회원 가입
]

