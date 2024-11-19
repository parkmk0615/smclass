from django.urls import path,include # include 추가
from . import views

app_name='students' # app이름 설정
urlpatterns = [
        # url 링크, views 함수호출, name 링크
    path('write/', views.write, name='write'),
    path('search/', views.search, name='search'), # 검색
    path('list/', views.list, name='list'),
    path('view/<str:name>/', views.view, name='view'),
    path('update/', views.update, name='update'), # 파라미터 형태
    #path('update/<str:name>/', views.update, name='update'),
    path('delete/<str:name>/', views.delete, name='delete'),
]
