from django.urls import path,include
from.import views
### 메인 URL ###
app_name="students"
urlpatterns = [
  
    path('',views.write2,name='write'),
]