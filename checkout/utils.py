from django.shortcuts import get_object_or_404
from .models import OrderLineItem
from products.models import Product
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET


def save_order_items(order, cart):
    """Save order to OrderLineItem model for admin panel purchase history"""
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        order_line_item = OrderLineItem(
            order=order,
            product=product,
            quantity=quantity
            )
        order_line_item.save()


def charge_card(stripe_token, total):
    """Charge test card in GBP under 'Dummy Transaction'"""
    total_in_pounds = int(total*100)
    return stripe.Charge.create(
        amount=total_in_pounds,
        currency="GBP",
        description="Dummy Transaction",
        card=stripe_token,
    )