from decimal import Decimal
from django.conf import settings
from goods.models import Goods
from django.shortcuts import render


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modifield = True

    def add_or_remove(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity,
                                     'price': str(product.price)}
            self.save()
        elif product_id in self.cart:
            del self.cart[product_id]
            self.save()



    def __iter__(self):
        goods_ids = self.cart.keys()
        goods = Goods.objects.filter(id__in=goods_ids)
        for good in goods:
            self.cart[str(good.id)]['product'] = good
            yield self.cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*Decimal(item['quantity']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modifield = True