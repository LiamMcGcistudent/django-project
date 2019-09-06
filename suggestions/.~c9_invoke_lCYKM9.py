from django.shortcuts import render, get_object_or_404, redirect
from .models import Suggestion, suggestionUpvote, SuggestionComment
from django.utils import timezone
from django.contrib import messages
from .forms import SuggestionForm, SuggestionCommentForm
from django.contrib.auth.decorators import login_required

def all_suggestions(request):
    """
    Displays all current suggestions
    """
    suggestions = Suggestion.objects.filter(created_date__lte=timezone.now())
    
    return render(request,'suggestions.html', {'suggestions':suggestions})
    
def single_suggestion(request, pk):
    """
    Displays a selected suggestion in more detail
    """
    suggestion = get_object_or_404(Suggestion, pk=pk)
    
    
    if request.method == 'POST':
        comment_form = SuggestionCommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = request.POST.get('comment')
            suggestion_comment = SuugestionComment.objects.create(suggestion=suggestion, posted_by=request.user, comment=comment)
            suggestion_comment.save()
            return redirect('single_suggestion', suggestion.pk)
    else:
        comment_form = SuggestionCommentForm
        suggestion.views +=1
        suggestion.save()
    
    comments = SuggestionComment.objects.filter(suggestion=suggestion)
    comment_form = SuggestionCommentForm()
    
    return render(request, 'suggestion_detail.html', {'suggestion':suggestion, 'comments': comments, 'comment_form': comment_form,})
    
@login_required
def make_suggestion(request):
    
    form = SuggestionForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.suggested_by = request.user
            suggestion.save()
            messages.success(request, 'Thank you, your suggestion has been added!', extra_tags="alert-success")
            
            return redirect('suggestions')
    else:
        form =SuggestionForm
        
    return render(request, 'make_suggestion.html', {'form':form})
    
@login_required
def upvote_suggestion(request, pk):
    """Adds one upvote point"""
    suggestion = get_object_or_404(Suggestion, pk=pk)
    suggestion.suggestion_upvotes += 1
    suggestion.views -= 1
    suggestion.save()

    try:
        upvote = get_object_or_404(
            suggestionUpvote, upvoted_suggestion=suggestion, user=request.user)
    except:
        upvote = suggestionUpvote()
    upvote.upvoted_suggestion = suggestion
    upvote.user = request.user
    upvote.save()
    return(redirect(single_suggestion, pk))
