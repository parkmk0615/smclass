from django.urls import path,include
from . import views

app_name="students"
urlpatterns = [
    path('write/', views.write, name="students" ),
    path('save/', views.save, name="save" ),
    path('list/', views.list, name="list" ),

]
