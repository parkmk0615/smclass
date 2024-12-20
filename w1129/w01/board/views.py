from django.shortcuts import render
from board.models import Board
from comment.models import Comment

# 상세보기
def bview(request,bno):
  qs = Board.objects.filter(bno=bno)
  # 하단 댓글 가져오기
  c_qs = Comment.objects.filter(board=qs[0]).order_by("-cno")
  context = {"board":qs[0],"clist":c_qs}
  print("확인: ",c_qs,c_qs.count)
  return render(request,'bview.html',context)


## 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)
