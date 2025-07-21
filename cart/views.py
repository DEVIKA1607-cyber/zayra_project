from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import CartItem, WishlistItem
from django.contrib.auth.decorators import login_required
from decimal import Decimal 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_view')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)

    tax_rate = Decimal('0.175') 
    tax = (total * tax_rate).quantize(Decimal('0.01'))
    grand_total = total + tax

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total
    })

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart:cart_view')


@csrf_exempt
@login_required
def add_to_wishlist(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        wishlist_item = WishlistItem.objects.filter(user=request.user, product=product).first()

        if wishlist_item:
            wishlist_item.delete()
            return JsonResponse({'status': 'removed'})
        else:
            WishlistItem.objects.create(user=request.user, product=product)
            return JsonResponse({'status': 'added'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

                        
@login_required
def remove_from_wishlist(request, product_id):
    item = WishlistItem.objects.filter(user=request.user, product__id=product_id).first()
    if item:
        item.delete()
    return redirect('cart:wishlist_view')

@login_required
def wishlist_view(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'cart/wishlist.html', {'wishlist_items': items})

