from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
	""" 
	Model for User
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to='main/profile/%Y/%m/%d/', blank=True)
	phone = models.CharField(max_length=15)
	reviews = models.IntegerField(default=0)
	joined = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.user.email