from django.shortcuts import render, redirect, get_object_or_404
from accounts.decorators import role_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DeliveryAssignment

def delivery_list(request):
    return render(request, 'delivery/delivery_list.html')


@login_required
def delivery_dashboard(request):
    if request.user.role != 'delivery':
        return redirect('home')  # or raise permission denied

    assignments = DeliveryAssignment.objects.filter(delivery_staff=request.user).select_related('order', 'order__user')

    return render(request, 'delivery/delivery_dashboard.html', {
        'deliveries': assignments
    })

@login_required
def mark_as_delivered(request, assignment_id):
    if request.method == 'POST':
        assignment = get_object_or_404(DeliveryAssignment, id=assignment_id, delivery_staff=request.user)

        if assignment.status == 'delivered':
            messages.info(request, "This order is already marked as delivered.")
        else:
            assignment.status = 'delivered'
            assignment.save()
            messages.success(request, "Order marked as delivered.")

        return redirect('delivery_dashboard')  # change if needed

    messages.error(request, "Invalid request.")
    return redirect('delivery_dashboard')