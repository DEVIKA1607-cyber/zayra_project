from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('COD', 'Cash on Delivery'),
        ('RAZORPAY', 'Razorpay'),
        ('STRIPE', 'Stripe'),
        ('PAYPAL', 'PayPal'),
        ('WALLET', 'Wallet Credits'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # or blank=True if needed
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_id = models.CharField(max_length=100, null=True, blank=True)  # Razorpay/Stripe ID
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.id} - {self.payment_method}"
