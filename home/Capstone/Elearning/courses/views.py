from django.shortcuts import render
from .models import Course 

from django.contrib.auth.decorators import login_required
# Create your views here.
def courses(request):
	courses=Course.objects.all 
	return render(request,'COURSE/courses.html',{'courses':courses})


@login_required
def course(request):
	id=request.GET.get('id', '')	

	course = Course.objects.get(pk=id)	
	return render(request,'COURSE/course_detail.html',{'course':course}) 


