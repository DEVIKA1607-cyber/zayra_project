from django.shortcuts import render, redirect
from accounts.decorators import role_required
from .models import DeliveryAssignment
from django.contrib.auth.decorators import login_required

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