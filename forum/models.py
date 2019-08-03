from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
	post = models.ForeignKey('forum.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=200)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	class Meta:
		ordering = ['-date_posted',]

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.content

