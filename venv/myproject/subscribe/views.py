from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubForm 
from .models import sub

def subscribe(request):
	emails = sub.objects.all()
	if request.method == 'POST':
		form = SubForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('E-mail')
			messages.success(request, f"Thanks for subscribing!")
			form.save()
			return redirect('home')
	else:
		form = SubForm()
			
	return render(request, "subscribe/subscribe.html", {'form':form, 'emails': emails})