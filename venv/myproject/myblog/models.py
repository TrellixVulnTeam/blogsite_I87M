from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	posted_in = models.DateTimeField(default= timezone.now)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title