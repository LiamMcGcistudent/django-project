from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

def get_reviews(request):
    """
    Create a view that will return a list
    of Reviews that were published prior to 'now'
    and render them to the 'reviews.html' template
    """
    
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(reviews, 5)
    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    return render(request, "reviews.html", {'reviews': reviews})

def full_review(request, pk):
    """
    Create a view that returns a single 
    Review Object based on the review ID (pk)
    and then render it to the 'reviewdetail.html' 
    template or return an error if the post is not found.
    """
    
    review = get_object_or_404(Review, pk=pk)
    
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment = request.POST.get('comment')
            review_comment = Comment.objects.create(review=review, author=request.user, comment=comment)
            review_comment.save()
            return redirect('full_review', review.pk)
    else:
        comment_form = CommentForm
        review.views +=1
        review.save()
    
    comments = Comment.objects.filter(review=review)
    comment_form = CommentForm()
    return render(request, "review.html", {'review': review, 'comments': comments, 'comment_form': comment_form,})

def create_or_edit_review(request, pk=None):
    """
    Create a view that allows us to create or edit a review,
    depending if the review ID is null or not.
    """
    
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.written_by = request.user
            review.save()
            return redirect(get_reviews)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviewform.html', {'form': form})
