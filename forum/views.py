from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostListView(ListView):
	model= Post
	template_name= 'forum/forum.html'
	context_object_name='posts'
	ordering=['-date_posted']

class PostDetailView(DetailView):
	model= Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model= Post
	fields=['title', 'content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model= Post
	fields=['title', 'content']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model= Post
	success_url = '/discussion_forum/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

@login_required
def add_comment_to_post(request, pk):
	
	form=CommentForm()
	post=get_object_or_404(Post, pk=pk)

	if request.method == "POST":
		form = CommentForm(request.POST)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.author=request.user
		comment.save()
		return redirect('post-detail', pk=post.pk)

	else:
		form = CommentForm()
	return render(request, 'forum/add_comment_to_post.html', {'form': form})


