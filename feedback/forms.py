from django import forms
from .models import Feedback

class feedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('first_name',
				  'last_name',
				  'email',
				  'ui',
				  'sug',
				  'satisfy',
				  'sugg',
				  'rating',
	        	  )