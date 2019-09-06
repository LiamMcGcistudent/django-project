from django import forms
from .models import Suggestion, SuggestionComment

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('title', 'content')
        
class SuggestionCommentForm(forms.ModelForm):
    class Meta:
        model = SuggestionComment
        fields = ('comment',)