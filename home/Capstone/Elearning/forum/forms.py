from django import forms
from .models import Comment
from django.forms import ModelForm

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		exclude= ('author', 'post', 'date_posted', 'approved_comment',)


	