
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from orders.models import Order, OrderItem
from payments.models import Payment
from django.utils import timezone
from django.urls import reverse
from delivery.utils import assign_least_busy_delivery_staff
from django.contrib import messages
from delivery.models import DeliveryAssignment


def order_list(request):
    return render(request, 'orders/user_order.html')

@login_required
def order_detail(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at')

    # Create a list of tuples: [(order, [items]), ...]
    order_data = []
    for order in orders:
        items = OrderItem.objects.filter(order=order)
        order_data.append((order, items))

    return render(request, 'orders/myorder.html', {'order_data': order_data})
@login_required

def track_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'prod_content/product_tracking.html', context)

@login_required
def place_order(request):
    if request.method == 'POST':
        user = request.user
        payment_method = request.POST.get('payment_method')

        # Get cart items
        cart_items = CartItem.objects.filter(user=user)
        if not cart_items.exists():
            return redirect('cart:cart_view')

        # Calculate total
        total = sum(item.product.price * item.quantity for item in cart_items)

        # Get and validate shipping address
        shipping_address = (request.POST.get('shipping_address') or '').strip()
        if not shipping_address or len(shipping_address) < 10:
            messages.error(request, "Please provide a valid shipping address.")
            return redirect('cart:cart_view')

        billing_address = (request.POST.get('billing_address') or 'No billing').strip()

        # Create Order
        order = Order.objects.create(
            user=user,
            shipping_address=shipping_address,
            billing_address=billing_address,
            total_amount=total
        )

        # Create OrderItems
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Create Payment
        Payment.objects.create(
            user=user,
            order=order,
            payment_method=payment_method,
            amount_paid=total,
            status='Pending' if payment_method == 'COD' else 'Completed',
            paid=True if payment_method != 'COD' else False
        )

        # Assign delivery staff
        assigned = assign_least_busy_delivery_staff(order)
        if assigned:
            print(f"Assigned to {assigned.username}")

        # Clear cart
        cart_items.delete()

        return redirect('order_success', order_id=order.id)

    return redirect('cart:cart_view')

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    
    # Example: Estimate delivery date 5 days from now
    from datetime import timedelta
    delivery_date = order.created_at + timedelta(days=5)

    return render(request, 'orders/order_success.html', {
        'order': order,
        'order_items': order_items,
        'order_id': order.id,
        'delivery_date': delivery_date.date()
    })


@login_required
def profile_panel(request):
    return render(request, 'profile_detail')

def checkout_view(request):
    last_order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    shipping_address = last_order.shipping_address if last_order else ''

    context = {
        'shipping_address': shipping_address,
        # your other context: cart items, total, etc.
    }
    return render(request, 'payments/payment.html', context)