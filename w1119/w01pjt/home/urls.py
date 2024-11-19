from django.urls import path,include # include 추가
from . import views

app_name='' # app이름 설정
urlpatterns = [
        # url 링크, views 함수호출, name 링크
    path('', views.index, name='index'),
]
