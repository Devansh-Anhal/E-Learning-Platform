from django.db import models



# Create your models here.
class Course(models.Model):
	title		= models.CharField(max_length=255)
	description = models.TextField(default='insert')
	logo		= models.ImageField(upload_to = "course",default='default.jpg', blank=True)
	instructor	= models.CharField(max_length=50)
	video       = models.FileField(upload_to = "course",null =True , blank =True)
	pdf         = models.FileField(upload_to = "course",null =True , blank =True)
	url			= models.CharField(max_length=255, default="#")
		
	def __str__(self):
		return self.title

	



