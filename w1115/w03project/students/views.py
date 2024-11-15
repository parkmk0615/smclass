from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student



### 학생 입력 페이지 호출
def write(request):
  return render(request,"stu_write.html")

###학생 입력 저장
def save(request):
  print("학생정보저장호출")

  if request.POST:
    print("post2")
    name=request.POST['name']
    major=request.POST['major']
    grade=request.POST['grade']
    age=request.POST['age']
    gender=request.POST['gender']

    print(name, major, grade, age, gender)

    qs=Student(s_name=name,s_major=major,s_age=age,s_gender=gender)
    qs.save()
  return HttpResponseRedirect(reverse('index'))


### 학생전체 리스트 호출
def list(request):
  qs=Student.objects.all()
  context={"list":qs}
  return render(request,'stu_list.html',context)