from django.contrib import admin
from students.models import Student

## admin관리자 페이지에서 컬럼 표시부분
class StudentAdmin(admin.ModelAdmin):
  list_display = ['s_name','s_major','s_age']

### admin사이트에 추가
admin.site.register(Student,StudentAdmin)

