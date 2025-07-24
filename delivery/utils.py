from django.db.models import Count
from accounts.models import User
from .models import DeliveryAssignment

def assign_least_busy_delivery_staff(order):
    delivery_staff_qs = User.objects.filter(role='delivery', is_active=True)

    # Use 'assignments' if you set related_name in your FK
    staff_with_assignments = delivery_staff_qs.annotate(
        assignment_count=Count('assignments')
    ).order_by('assignment_count')

    if staff_with_assignments.exists():
        selected_staff = staff_with_assignments.first()
        DeliveryAssignment.objects.create(
            order=order,
            delivery_staff=selected_staff,
            status='pending'
        )
        print("Assigned to:", selected_staff.username)  # Debug
        return selected_staff
    return None
