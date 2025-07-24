from django.db.models import Count
from accounts.models import User
from .models import DeliveryAssignment

def assign_least_busy_delivery_staff(order):
    # Get all active delivery staff
    delivery_staff_qs = User.objects.filter(role='delivery', is_active=True)

    # Annotate with correct related name: 'deliveryassignment'
    staff_with_assignments = delivery_staff_qs.annotate(
        assignment_count=Count('deliveryassignment')
    ).order_by('assignment_count')

    # Assign to the least busy staff
    if staff_with_assignments.exists():
        selected_staff = staff_with_assignments.first()
        DeliveryAssignment.objects.create(
            order=order,
            delivery_staff=selected_staff,
            status='pending'
        )
        return selected_staff
    return None
