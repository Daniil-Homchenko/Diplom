from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from goods import models
from .cart import Cart
from .forms import CartAddProductForm




# Create your views here.

#@require_POST
def cart_add_or_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(models.Goods, id=id)
    cart.add_or_remove(product)
    goods = models.Goods.objects.all()
    return redirect('cart:cart_detail')

def clear_cart(request):
    cart =Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    goods = models.Goods.objects.all()
    return render(request, 'detail.html', {'cart': cart,
                                           'goods': goods})
