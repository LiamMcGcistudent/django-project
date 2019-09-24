from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from suggestions.models import Suggestion

class UserProfile(models.Model):
	""" 
	Model for User
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	joined = models.DateTimeField(default=datetime.now, blank=True)
	suggestion_upvotes = models.ForeignKey(Suggestion, on_delete=models.CASCADE, default=0)
	def __str__(self):
		return self.user.email