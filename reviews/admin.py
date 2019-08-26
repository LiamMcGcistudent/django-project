from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'content', 'published_date']

admin.site.register(Review)