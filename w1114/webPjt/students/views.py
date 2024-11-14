from django.shortcuts import render

# Create your views here.
def write1(request):
  return render(request,'write.html')