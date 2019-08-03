from django.shortcuts import render
from .models import Instructor

# Create your views here.
def instruc(request):
	ins = Instructor.objects.all 
	return render(request,'instructo.html',{'ins':ins})
