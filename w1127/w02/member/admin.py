from django.contrib import admin
from member.models import Students

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
  list_display = ['id','name','nicname','gender']
