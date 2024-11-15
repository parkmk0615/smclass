from django.urls import path,include
from . import views

app_name ='students' # app 이름 : 이름으로 접근
urlpatterns = [
    # views.py연결 - 함수 호출, app함수이름
    path('write/',views.write, name='write'),
    path('save/',views.save, name='save'),
    path('list/',views.list, name='list'),
]
