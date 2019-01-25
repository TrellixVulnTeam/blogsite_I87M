from django.db import models

class sub(models.Model):
	email = models.EmailField()

	def __str__():
		return self.email