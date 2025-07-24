
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from orders.models import Order, OrderItem
from payments.models import Payment
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from delivery.utils import assign_least_busy_delivery_staff


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

        # Create Order
        order = Order.objects.create(
            user=user,
            shipping_address=request.POST.get('shipping_address', 'No address'),
            billing_address=request.POST.get('billing_address', 'No billing'),
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

        assigned = assign_least_busy_delivery_staff(order)
        if assigned:
            print(f"Assigned to {assigned.username}")

        # Delete cart items only after order is created successfully
        cart_items.delete()

        # Redirect to success page with order ID
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
