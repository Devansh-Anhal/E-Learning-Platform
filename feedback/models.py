from django.core.validators import RegexValidator

from django.db import models


class Feedback(models.Model):
	choice = (
					('y', 'Yes'),
					('n', 'No'),
				)
	cc = (
					('a', '1'),
					('b', '2'),
					('c', '3'),
					('d', '4'),
					('e', '5'),
				)

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	ui = models.CharField("Did you like UI of our website", max_length=30, choices = choice)
	sug = models.TextField("Suggest some changes in the website", default="")
	satisfy = models.CharField("Are you satisfied with course content",  max_length=30, choices = choice)
	sugg = models.TextField("Suggest some changes in course content or any additions", default="")
	rating = models.CharField("Rate your experience", max_length=10, choices = cc)
	
	def __str__(self):
		return self.first_name + " " + self.last_name
