from django.contrib import admin
from .models import Suggestion, Upvotes

# Register your models here.

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'suggested_by', 'published_date', 'status', 'suggestion_upvotes']
    list_filter = ['status',]
    
admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Upvotes)