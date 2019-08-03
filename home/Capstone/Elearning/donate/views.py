from django.shortcuts import render

# Create your views here.
def pay(request):
	return render(request, 'payment.html')