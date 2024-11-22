from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # home app 연결
    path('board/', include('board.urls')), # board app 연결

]
