from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_to_cart(request):
    if request.method == "POST":
        product = {
            'name': request.POST.get('product_name'),
            'price': request.POST.get('product_price'),
            'image': request.POST.get('product_img'),
        }
        cart = request.session.get('cart', [])
        cart.append(product)
        request.session['cart'] = cart
        return redirect('cart')


def cart_view(request):
    cart_items = request.session.get('cart', [])
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

def wishlist_view(request):
    return render(request, 'cart/wishlist.html')