from django.urls import path,include
from . import views

app_name="member"
urlpatterns = [
  ## 로그인 관련
    path('login/',views.login, name="login"), # 로그인
    path('logout/',views.logout, name="logout"), # 로그아웃 

  ## 회원정보 관련
    path('mlist/',views.mlist, name="mlist"), # 회원 리스트 페이지
    path('mview/<str:id>/',views.mview, name="mview"), # 회원상세 페이지
    path('mupdate/<str:id>/',views.mupdate, name="mupdate"), # 회원정보 수정
    path('mwrite/',views.mwrite, name="mwrite"), # 회원정보 입력
    path('mdelete/<str:id>/',views.mdelete, name="mdelete"), # 회원정보삭제
]
