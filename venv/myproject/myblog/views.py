from django.shortcuts import render
from . import templates
from .models import post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
	context = {
		'post': post.objects.all()
		}
	return render(request, 'myblog/home.html', context)

class PostListView(ListView):
	model = post
	template_name = 'myblog/home.html'
	context_object_name = 'post'
	ordering = '-posted_in'

class PostDetailView(DetailView):
	model = post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = post
	fields= ['title', 'content']

def about(request):
	return render(request, "myblog/about_me.html")