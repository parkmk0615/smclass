from django.shortcuts import render,redirect
from member.models import Member

def logout(request):
  # 세션 모두 삭제
  request.session.clear() # 세션 모두 삭제
  # del request.session['session_id'] # 해당 세션 1개 삭제
  return redirect('index')


def login(request):
  if request.method =="GET":
    response = render(request,'login.html')
  else:
    emsg=""
    id =request.POST.get("id")
    pw =request.POST.get("pw")
    qs=Member.objects.filter(id=id, pw=pw)
    if qs: 
      context= {"emsg":emsg,"member":qs[0]}
      request.session['session_id'] = id
      request.session['session_nicName'] = qs[0].nicName
      response = render(request,'index.html',context)
    else:
      emsg="아이디 또는 패스워드가 일치 하지 않습니다."
      context= {"emsg":emsg,"member":""}
      response = render(request,'login.html',context)

  return response



def cookDelete(request):
  if request.method == "GET":
    response = render(request,'cookDelete.html')
    return response
  else:
    response = render(request,'index.html')
    c = request.POST.get('ckey')
    print(c)
    response.delete_cookie(c)
    print(c,"쿠키가 삭제되었습니다.")
  return response


def cookWrite(request):
  response = render(request,'cookWrite.html')
  if request.method =="GET":
    print("GET방식으로 들어옴")
  else:
    print("POST방식으로 들어옴")
    response = render(request,'index.html')
    ckey=request.POST.get('ckey')
    cvalue=request.POST.get('cvalue')
    response.set_cookie(ckey,cvalue)

  return response


def mlist(request):
  return render(request,'mlist.html')

