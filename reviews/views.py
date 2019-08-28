from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Review
from .forms import ReviewForm

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
    review.views +=1
    review.save()
    return render(request, "review.html", {'review': review})

def create_or_edit_review(request, pk=None):
    """
    Create a view that allows us to create or edit a review,
    depending if the review ID is null or not.
    """
    
    review = get_object_or_404(Review, pk=pk) if pk else None
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect(full_review, review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviewform.html', {'form': form})