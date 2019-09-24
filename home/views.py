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
    todo_no = Suggestion.objects.filter(status='To do').count()
    inprogress_no = Suggestion.objects.filter(status='In progress').count()
    complete_no = Suggestion.objects.filter(status='Complete').count()
    suggestion_labels = ['To Do', 'In Progress', 'Complete']
    suggestion_count = [todo_no, inprogress_no, complete_no]

    suggestions = Suggestion.objects.order_by('-suggestion_upvotes')[:5]
    upvote_labels = []
    upvote_count = []
    for suggestion in suggestions:
        upvote_labels.append(suggestion.title)
        upvote_count.append(suggestion.suggestion_upvotes)

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