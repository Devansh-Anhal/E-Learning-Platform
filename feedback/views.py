from django.shortcuts import render
from .forms import feedbackForm
# Create your views here.
def feed(request):
	template="feedback.html"

	if request.method == "POST":
		form = feedbackForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = feedbackForm()

	context = {
		'form' : form ,
	}			

	return render(request, template, context)