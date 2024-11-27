from django.shortcuts import render,redirect
from member.models import Students

# 로그아웃
def logout(request):
  request.session.clear() # 모든 섹션 삭제 / del request.session['session_id'] : 1개삭제
  context={"lsmg":"1"}
  return render(request,'index.html',context)

# 로그인
def login(request):
  if request.method =="GET": 
    return render(request,'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Students.objects.filter(id=id,pw=pw)

    if qs:
      request.session['session_id']=id
      request.session['session_nicname']=qs[0].nicname
      
      context = {"lmsg":"1"}
      return render(request,'login.html',context)
    else:
      context = {"lmsg":"0"}
      return render(request,'login.html',context)