from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
	""" 
	Model for User
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.TextField(max_length=20)
	last_name = models.TextField(max_length=50)
	profile_image = models.FileField(upload_to='images', blank=True)
	joined = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.user.email