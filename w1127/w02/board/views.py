from django.shortcuts import render
from board.models import Board
from member.models import Students

# 글 상세보기
def bview(request,bno):
  npage=request.GET.get("npage",1)
  qs= Board.objects.get(bno=bno)
  context={"board":qs}
  ## 이전글, 다음글

  # 조회수 증가방지, 날짜 설정 - 쿠키기간사용

  # 쿠키확인
  
  # 조회수 증가
  qs.bhit +=1
  qs.save()
  return render(request,'bview.html',context)


# 글쓰기
def bwrite(request):
  if request.method =="GET":
    return render(request,'bwrite.html')
  else:
    id = request.session['session_id']
    member =Students.objects.get(id=id)
    btitle=request.POST.get("btitle")
    bcontent=request.POST.get("bcontent")
    bfile=request.FILES.get("bfile","")
    print("파일정보 : ",bfile)
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context={'wmsg':"1"}
    return render(request, 'bwrite.html',context)



# 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)