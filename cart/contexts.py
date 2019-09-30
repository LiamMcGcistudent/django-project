from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(cart):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    totals = 0
    products = []

    for item in cart:
        product = get_object_or_404(Product, pk=item)
        products.append({
            'product': product,
            'quantity': cart[item],
            'price': product.price,
            'total': (cart[item] * product.price)
        })
        totals += cart[item] * product.price
    return {'cart': products, 'totals': totals}