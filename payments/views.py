from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import random
from datetime import datetime, timedelta
from cart.models import CartItem
from orders.models import Order

@csrf_exempt
def payment_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    item_count = cart_items.count()
    delivery_charge = 6
    discount = 0

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    total = subtotal + delivery_charge - discount

    shipping_address = ""

    if request.method == "POST":
        shipping_address = request.POST.get('shipping_address')

        # Create and save the order
        order = Order.objects.create(
            user=request.user,
            shipping_address=shipping_address,
            total_amount=total
        )
        # You can also redirect to payment success or next step
        return redirect('upi_page')  # or 'success_page' depending on flow

    context = {
        'item_count': item_count,
        'delivery_charge': delivery_charge,
        'subtotal': subtotal,
        'discount': discount,
        'order_total': total,
        'shipping_address': shipping_address,
    }
    return render(request, 'payments/payment.html', context)

@csrf_exempt
def upi_page(request):
    if request.method == 'POST':
        amount = request.POST.get('amount', 0)
        return render(request, 'payments/upi.html', {'amount': amount})
    return redirect('payment')

@csrf_exempt
def success_page(request):
    if request.method == 'POST':
        order_id = random.randint(30000, 99999)
        delivery_date = datetime.now() + timedelta(days=2)
        return render(request, 'payments/success.html', {
            'order_id': order_id,
            'delivery_date': delivery_date.strftime('%B %d, %Y')
        })
    return redirect('payment')