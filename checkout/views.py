from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from cart.contexts import cart_contents
from django.utils import timezone
from products.models import Product
import stripe
from .utils import save_order_items, charge_card


# Create your views here.

@login_required()
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if request.method == "POST":
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)

            if order_form.is_valid() and payment_form.is_valid():
                # Save The Order
                order = order_form.save(commit=False)
                order.date = timezone.now()
                order.save()

                # Save the Order Line Items
                cart = request.session.get('cart', {})
                save_order_items(order, cart)

                # Charge the Card
                items_and_total = cart_contents(request)
                total = items_and_total['total']
                stripe_token = payment_form.cleaned_data['stripe_id']

                try:
                    customer = charge_card(stripe_token, total)
                except stripe.error.CardError:
                    messages.error(request, "Your card was declined!", extra_tags="alert-danger")
                    
                try:
                    if customer.paid:
                         messages.error(request, "You have successfully paid", extra_tags="alert-success")
                         request.session['cart'] = {}
                         return redirect(reverse('products'))
                    
                    # Clear the Cart
                    del request.session['cart']
                    return redirect('products')
                except: 
                    messages.error(request, "Unable to take payment", extra_tags="alert-warning")

                    

            else:
                order_form = OrderForm()
                payment_form = MakePaymentForm()
                context = {'order_form': order_form,
                           'payment_form': payment_form,
                           'publishable': settings.STRIPE_PUBLISHABLE}
                cart = request.session.get('cart', {})
                cart_items_and_total = cart_contents(request)
                context.update(cart_items_and_total)
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
                
            
