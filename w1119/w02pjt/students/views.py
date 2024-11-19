from django.shortcuts import render,redirect
from students.models import Student

# 학생 등록
def write(request):
  if request.method == "POST":
    name=request.POST.get('name')
    major=request.POST.get('major')
    grade=request.POST.get('grade')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    hobby=request.POST.getlist('hobby')
  
    print(name)
    print(hobby)

    qs=Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby)
    qs.save()
    return redirect('/students/list/')
  
  else:
    return render(request,'write.html')
  

# 학생 전체 리스트
def list(request):
  qs=Student.objects.all()
  context={"slist":qs,}
  return render(request,'list.html',context)

# 학생 상세보기
def view(request,name):
  qs=Student.objects.get(name=name)
  context={"stu":qs}
  return render(request,'view.html',context)

# 학생정보 수정, 수정 정보 저장
def update(request):
  if request.method=="GET":
    name=request.GET['name']
    print(name)
    qs=Student.objects.get(name=name)
    context={"stu":qs}
    return render(request,'update.html',context)
  else:
    name=request.POST.get('name')
    major=request.POST.get('major')
    grade=request.POST.get('grade')
    age=request.POST.get('age')
    gender=request.POST.get('gender')
    hobby=request.POST.getlist('hobby')

    # Student검색
    qs=Student.objects.get(name=name)
    qs.major=major
    qs.grade=grade
    qs.age=age
    qs.gender=gender
    qs.hobby=hobby
    qs.save()

    return redirect('students:view',name)
