from django.db import models
from orders.models import Order

class Payment(models.Model):
    STATUS_CHOICES = [
        ('Success', 'Success'),
        ('Failed', 'Failed'),
        ('Refunded', 'Refunded'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50)
