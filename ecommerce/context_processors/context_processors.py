import json
from store.models import Order, Customer


def total_cart_items(request):
    if request.user.is_authenticated:
        customer = Customer.objects.filter(user=request.user).first()

        if customer is None:
            return {"totalCartItems": 0}

        order = Order.objects.filter(customer=customer, ordered=False).first()

        if order is None:
            return {"totalCartItems": 0}

        cartItems = order.get_cart_items

    else:
        try:
            cart = json.loads(request.COOKIES["cart"])
        except:
            cart = {}

        items = []
        cartItems = 0

        for i in cart:
            try:
                cartItems += cart[i]["quantity"]

            except:
                pass

    return {"totalCartItems": cartItems}
