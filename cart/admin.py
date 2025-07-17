from django.contrib import admin
from .models import CartItem  # Model from models.py

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'saved_for_later', 'added_at')
    list_filter = ('saved_for_later',)
    search_fields = ('user__username', 'product__name')
