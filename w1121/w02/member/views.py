from django.shortcuts import render,redirect
from member.models import Member

#회원가입2
def join02(request):
  return render(request,'join02.html')

#회원가입1
def join01(request):
  return render(request,'join01.html')

def logout(request):
  request.session.clear()
  return redirect("/")


def login(request):
  if request.method=="GET":
    return render(request,'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs= Member.objects.filter(id=id,pw=pw)
    if qs:
      msg="로그인이 되었습니다."
      print(msg)
      request.session['session_id'] = id
      request.session['session_nickname'] = qs[0].nickname
      return redirect('index')
    else:
      msg="아이디 또는 패스워드가 일치하지 않습니다.."
      print(msg)
      return render(request,'login.html',{"login_msg":msg})