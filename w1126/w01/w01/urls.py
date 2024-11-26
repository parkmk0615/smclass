from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('member/', include('member.urls')),
    path('board/', include('board.urls')),
]

# settings.py 안에 media url로 들어오면, media 폴더에서 검색
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)