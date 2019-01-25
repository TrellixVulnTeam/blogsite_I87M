from django.forms import ModelForm
from .models import sub

class SubForm(ModelForm):
	class Meta:
		model = sub
		fields = ['email',]