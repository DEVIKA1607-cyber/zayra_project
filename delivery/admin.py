from django.contrib import admin
from .models import Delivery  # Model from models.py

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_staff', 'delivery_status', 'confirmed_at')
    list_filter = ('delivery_status',)
    search_fields = ('order__id', 'delivery_staff__username')
