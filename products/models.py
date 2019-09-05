from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    is_published = models.BooleanField(default=False)
    added = models.DateTimeField(blank=True, default=datetime.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
