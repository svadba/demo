from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
# from cupons.forms import CuponApllyForm

# Эта вьюха добавляет товар в корзину. В качестве параметра она принимает запрос и идентификатор товара.
@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, update_quantity=cd['update'])
        # cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:CartDetail')


# Эта вьюха удаляет товар из корзины. В качестве параметра она принимает запрос и идентификатор товара.
def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')

# Эта функция получает экземпляр корзины пользователя и передает его в качестве параметра в шаблон.
def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
