from django.contrib import admin
from .models import Payment  # Model from models.py

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'status', 'method', 'payment_date')
    list_filter = ('status', 'method')
    search_fields = ('order__id',)
