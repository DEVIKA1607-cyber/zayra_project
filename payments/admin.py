from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_method', 'amount_paid', 'paid', 'created_at']
    list_filter = ['payment_method', 'paid']
    search_fields = ['order__id', 'payment_id']
