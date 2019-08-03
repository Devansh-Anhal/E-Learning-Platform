from django.db import models

# Create your models here.
class Instructor(models.Model):
	name = models.CharField(max_length= 50)
	image = models.ImageField(upload_to="instruct" , default="default.jpg" )
	url   = models.CharField(max_length=255, default="#")

	def __str__(self):
		return self.name
