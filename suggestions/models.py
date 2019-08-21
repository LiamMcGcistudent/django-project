from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Suggestion(models.Model):
    """
    A single suggestion
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    
    
    def __unicode__(self):
        return self.title