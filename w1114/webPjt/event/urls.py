from django.urls import path,include
from.import views
### 메인 URL ###
app_name="event"
urlpatterns = [
  
    path('event/',views.write1,name='eventview'),
]

