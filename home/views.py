from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from products.models import Product
from suggestions.models import Suggestion


def index(request):
    """A view that displays the index page"""
    
    return render(request, "index.html")
    
def graphs(request):
    return render(request, 'graphs.html')


def graph_data(request):
    todo_no = Suggestion.objects.filter(fix_status='ToDo').count()
    doing_no = Suggestion.objects.filter(fix_status='Doing').count()
    done_no = Suggestion.objects.filter(fix_status='Done').count()
    suggestion_labels = ['todo', 'doing', 'done']
    suggestion_count = [todo_no, doing_no, done_no]

    suggestions = Suggestion.objects.order_by('-upvote')[:5]
    upvote_labels = []
    upvote_count = []
    for suggestion in suggestions:
        upvote_labels.append(suggestion.title)
        upvote_count.append(suggestion.upvote)

    products = Product.objects.order_by('-views')[:5]
    view_labels = []
    view_count = []
    for product in products:
        view_labels.append(product.name)
        view_count.append(product.views)

    data = {
        
        'suggestion_labels': suggestion_labels,
        'suggestion_count': suggestion_count,
        'upvote_labels': upvote_labels,
        'upvote_count': upvote_count,
        'view_labels': view_labels,
        'view_count': view_count,
    }
    return JsonResponse(data)