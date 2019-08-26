from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Suggestion(models.Model):
    """
    A single suggestion
    """
    STATUS_CHOICES = (
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Complete', 'Complete')
        )
    
    title = models.CharField(max_length=50)
    content = models.TextField(blank=False)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='To do')
    suggested_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    suggestion_upvotes = models.IntegerField(default=0)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title
        
class Upvotes(models.Model):
    """Bug upvotes"""
    upvote_user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(Suggestion, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Up votes"
    
    def __str__(self):
        return self.upvote_user.username
        
    
    