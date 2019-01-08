from django.shortcuts import render
from . import templates
from .models import post
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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

class PostCreateView(LoginRequiredMixin, CreateView):
	model = post
	fields= ['title', 'content']


class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = post
	fields= ['title', 'content']


class PostDetailView(DetailView):
	model = post

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = post
	success_url = reverse_lazy('home')


def about(request):
	return render(request, "myblog/about_me.html")