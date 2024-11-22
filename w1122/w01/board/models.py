from django.db import models

class Board(models.Model):
  bno = models.AutoField(primary_key=True) # 게시판번호
  id = models.CharField(max_length=100)
  # member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
  btitle = models.CharField(max_length=1000) # 제목

  bcontent = models.TextField()             # 내용

  bgroup = models.IntegerField(null=True)   # 답글을 사용할때 그룹 핑

  bstep = models.IntegerField(default=0)    # 답글을 사용할때 순서
 
  bindent = models.IntegerField(default=0)  # 답글을 사용할때 들여쓰기
  
  bhit = models.IntegerField(default=0)     # 조회수

  bdate = models.DateTimeField(auto_now=True) # 날짜

  def __str__(self):
    return f"{self.bno},{self.id},{self.btitle},{self.bdate}"