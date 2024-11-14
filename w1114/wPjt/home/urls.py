from django.urls import path,include
from.import views
### 메인 URL ###
app_name="home"
urlpatterns = [
  
    path('',views.write3,name='home'),
]