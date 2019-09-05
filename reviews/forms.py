from django import forms
from .models import Review, ReviewComment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        
class CommentForm(forms.ModelForm):
    model = ReviewComment
    fields = ('comment',)