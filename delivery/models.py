from django.db import models
from orders.models import Order
from accounts.models import User

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_staff = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'delivery'})
    delivery_status = models.CharField(max_length=50, default='Assigned')
    delivery_otp = models.CharField(max_length=6)
    confirmed_at = models.DateTimeField(auto_now_add=True)
