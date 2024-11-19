from django.shortcuts import render,redirect
from students.models import Student
from django.urls import reverse


# 학생입력페이지 열기, 학생저장
def write(request):
  if request.method == "POST":
    name = request.POST.get('name') # 첫번째방법  // 데이터 없으면 None
    major = request.POST.get('major')
    grade = request.POST['grade'] # 두번째방법  // 데이터가 없으면 에러 발생
    age = request.POST['age'] 
    gender = request.POST['gender'] 
    # hobby = request.POST['hobby'] # 1개 밖에 못가져옴
    hobbys = request.POST.getlist('hobby') # 여러개 가져올 수 있음
    #hobby = ','.join(hobbys)      # list -> str타입으로 변경
    #hobby_list = hobby.split(",") # str -> list타입으로 변경

    print(name)
    # print("hobby 단일 : ",hobby)
    print("hobbys 복수 : ",hobbys)

    ## qs.save()
    qs=Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
    qs.save()

    ## create() : save() 필요없음
    # Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)

    return redirect('/students/list/')

  else: # GET호출

    # templates 폴더에서 html 파일 검색
    return render(request,'write.html')
  
# 학생리스트
def list(request):
  qs = Student.objects.order_by()
  context={"slist":qs,}
  return render(request,'list.html',context)

# 학생 상세보기
def view(request,name):
  qs=Student.objects.get(name=name)
  context={"stu":qs}
  return render(request,'view.html',context)


# 학생 수정페이지, 학생 수정저장
def update(request):
  if request.method == "GET":
    name=request.GET['name']
    print(name)
    qs=Student.objects.get(name=name)
    context={"stu":qs}
    return render(request,'update.html',context)
  else:
    name =request.POST.get('name')
    major =request.POST.get('major')
    grade =request.POST.get('grade')
    age =request.POST.get('age')
    gender =request.POST.get('gender')
    hobby =request.POST.getlist('hobby')

    # Student 검색
    qs= Student.objects.get(name=name)
    qs.major=major
    qs.grade=grade
    qs.age=age
    qs.gender=gender
    qs.hobby=hobby
    qs.save()

    return redirect('students:view',name)
   #return redirect(reverse('students:view',args=(name,)))


# 학생 정보삭제
def delete(request,name):
  print("삭제정보 이름:",name)
  Student.objects.get(name=name).delete()
  return redirect('/students/list')

# 학생검색
def search(request):
  search = request.GET.get('search')
  print("검색 단어 search : ",search)
  # 데이터검색
  #qs=Student.objects.filter(name=search)
  qs=Student.objects.filter(name__contains=search)
  context={"slist":qs}
  return render(request, 'list.html',context)