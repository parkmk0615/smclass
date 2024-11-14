from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    ### url students 들어오면 students > urls.py
    path('students/',include('students.urls')),
    path('event/',include('event.urls')),
    path('',include('home.urls')),
]

