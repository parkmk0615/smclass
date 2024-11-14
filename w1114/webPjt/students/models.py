from django.db import models

# Create your models here.
## db오라클에서 table 생성가능, insert,update,delete,select
## 오라클에 접속하지 않고도 테이블 생성 가능
## orm(object-relational mapping) 객체관계형 매핑

class students(models.Model):
  s_name = models.CharField(max_length=100)
  s_major = models.CharField(max_length=100)
  s_age = models.IntegerField(default=0)
  s_grade= models.IntegerField(default=0)
  s_gender=models.CharField(max_length=30)

  def __str__(self):
    return self.s_name