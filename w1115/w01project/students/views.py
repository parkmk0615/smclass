from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

### 학생 전체 리스트 호출
def list(request):
  # 학생전체리스트 가져오기
  qs=Student.objects.all()
  # 정보전변수생성
  context={"list":qs}
  return render(request,'stu_list.html',context)

### 학생 입력 페이지 호출
def write(request):
  print("학생등록페이지 호출")
  return render(request,"stu_write.html")

### 학생 입력 저장
def save(request):
  print("학생정보저장호출")
  
  
  #if request.POST == 'POST': // POST방식으로 왔는지 체크
  if request.POST: # request방식으로 왔는지 체크 
    print("post2")
    name=request.POST['name']
    major=request.POST['major']
    grade=request.POST['grade']
    age=request.POST['age']
    gender=request.POST['gender']
    print(name,major,grade,age,gender)
    qs=Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    qs.save()
  return HttpResponseRedirect(reverse('index'))
  #return redirect('index')
  #return redirect(reverse('index')) 