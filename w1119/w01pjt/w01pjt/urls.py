from django.contrib import admin
from django.urls import path,include # include 추가

urlpatterns = [
    path('admin/', admin.site.urls), # admin관리자 사이트 링크
    path('students/', include('students.urls')), # students 사이트 링크
    path('', include('home.urls')), # home 사이트 링크
]
