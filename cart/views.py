from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import CartItem

@csrf_exempt
@login_required
def add_to_cart(request):
    if request.method == "POST":
        # Session cart (for UI)
        product_data = {
            'name': request.POST.get('product_name'),
            'price': request.POST.get('product_price'),
            'image': request.POST.get('product_img'),
        }
        session_cart = request.session.get('cart', [])
        session_cart.append(product_data)
        request.session['cart'] = session_cart

        # ORM cart (DB)
        product_name = request.POST.get('product_name')
        try:
            product_obj = Product.objects.get(name=product_name)
        except Product.DoesNotExist:
            return redirect('cart')  # skip ORM if not found

        existing_item = CartItem.objects.filter(user=request.user, product=product_obj).first()
        if existing_item:
            existing_item.quantity += 1
            existing_item.save()
        else:
            CartItem.objects.create(user=request.user, product=product_obj, quantity=1)

        return redirect('cart')

def cart_view(request):
    cart_items = request.session.get('cart', [])
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

def wishlist_view(request):
    return render(request, 'cart/wishlist.html')