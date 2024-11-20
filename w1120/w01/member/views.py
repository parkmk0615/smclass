from django.shortcuts import render
from member.models import Member


def m2(request):
  if request.method =="GET":
    # 쿠키 읽어오기
    info1=request.COOKIES.get('info1','')
    info2=request.COOKIES.get('info2','')
    info3=request.COOKIES.get('info3','')
    context={"info1":info1,"info2":info2,"info3":info3}
    return render(request,'m2.html',context)
  else:
    #쿠키저장
    response=render(request,'index.html')
    memberId=request.POST.get('memberId')
    money=request.POST.get('money')
    option=request.POST.get('option')
    saveMember=request.POST.get('saveMember')
    if saveMember is not None:
      #쿠키저장
      response.set_cookie('info1',memberId,max_age=60*60)
      response.set_cookie('info2',money,max_age=60*60)
      response.set_cookie('info3',option,max_age=60*60)
    else:
      response.delete_cookie('info1')
      response.delete_cookie('info2')
      response.delete_cookie('info3')
    return response


def product(request):
  if request.method == "GET":
    #쿠키 읽어오기
    cookId2=request.COOKIES.get('cookId2','')
    cookId3=request.COOKIES.get('cookId3','')
    context={"cookId2":cookId2,'cookId3':cookId3}
    return render(request,'product.html',context)
  else:
    #쿠키저장
    response=render(request,'index.html')
    pId=request.POST.get('pId')
    pName=request.POST.get('pName')
    saveProduct=request.POST.get('saveProduct')
    if saveProduct is not None: # 체크가 되어 있으면
      # 쿠키 저장
      response.set_cookie('cookId2',pId,max_age=60*60)
      response.set_cookie('cookId3',pName,max_age=60*60)
    else:
      response.delete_cookie('cookId2')
      response.delete_cookie('cookId3')
    return response



def login2(request):
  if request.method == "GET":
    cookId=request.COOKIES.get('cookId','')
    context={"cookId":cookId}
    return render(request,'login2.html',context)
    
  else:
    response=render(request,'index.html')
    # 3개 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')
    if saveId is not None:
      response.set_cookie('cookId',id,max_age=60*60)
    else: 
      response.delete_cookie('cookId')
    return response



# 로그인 페이지
## 쿠키 정보검색 : request.COOKIES.get('이름')
## 쿠키저장 : response.set_coolis('key','value')
## 쿠키 삭제 : repone.delete_cookie('key')
def login(request):
  if request.method == "GET":
    print("쿠키정보: ",request.COOKIES)
    print("cookinfo 쿠키정보: ",request.COOKIES.get('cookinfo'))
    saveId=request.COOKIES.get('saveId','')
    print("saveId : ",saveId)
    context={"saveId":saveId}
    response=render(request,'login.html',context)
    # 쿠키설정(저장)
    # max_age가 없으면 브라우저 종료 시 삭제, max_age=60초*60분삭제  // 1달유지 = 60초*60분*24시간*30일
    ## 쿠키 정보 검색
    if not request.COOKIES.get('cookinfo'):
      response.set_cookie('cookinfo','1111',max_age=60*60) 
    return response
  else:
    print("쿠키정보 : ",request.COOKIES)
    id=request.POST.get("id")
    pw=request.POST.get("pw")
    # pw=request.POST["pw"] # 값 없을 경우 에러 발생
    saveId=request.POST.get("saveId", "값 없음")
    print("전달받은 정보 : ", id,pw,saveId)
    response=render(request,'login.html')
    ## id 기억하기 정보가 있으면 
    if saveId is not None: 
      response.set_cookie('saveId',id,max_age=60*60) # 아이디 기억하기가 체크가 되어 있으면 쿠키 저장
    else: 
      response.delete_cookie('saveId') # 아이디 기억하기가 체크가 되어 있지 않으면 쿠키 삭제
    return response


# 회원전체리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context={"mlist":qs}
  return render(request,'mlist.html',context)
