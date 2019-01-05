from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubForm as sub

def subscribe(request):
	if request.method == 'POST':
		form = sub(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('email')
			messages.success(request, f"Thanks for subscribing!")
			form.save()
			return redirect('home')
	else:
		form = sub()
			
	return render(request, "subscribe/subscribe.html", {'form':form})