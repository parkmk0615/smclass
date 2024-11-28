from django.shortcuts import render
from member.models import Member
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입


def idChk(request):
  id = request.POST.get("id","")
  qs = Member.objects.filter(id=id)
  qs_list = list(qs.values())
  if not qs:
    context={"result":"success"}
  else:
    context={"result":"false","member":qs_list}
    
  return JsonResponse(context)


# 회원가입 03
def step03(request):
  return render(request,'step03.html')



# 로그인체크
# json 타입으로 변경하려면 리스트 타입 또는 딕셔너리 타입으로 변경이 되어야 한다. // qs:set 타입 -> 리스트 타입으로 변경
## @csrf_exempt  # 예외처리
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  qs = Member.objects.filter(id=id,pw=pw) # 없으면 None
  if qs:
    print("성공")
    request.session['session_id'] = id
    request.session['session_nicName'] = qs[0].nicName
    qs_list = list(qs.values())
    context ={"result":"success","member":qs_list}
  else:
    print("실패")
    context={"result":"fail"}

    # qs = Member.objects.get(id=id,pw=pw)    # 없으면 에러
    # json_qs= serializers.serialize('json',[qs]) # json 타입변경
  return JsonResponse(context)

# 로그아웃
def logout(request):
  request.session.clear()   # <-모두 삭제 // 1개 삭제 : del request.session['session_id'] 
  context={"outmsg":"1"}
  return render(request,'index.html',context)

# 로그인
def login(request):
  return render(request,'login.html')