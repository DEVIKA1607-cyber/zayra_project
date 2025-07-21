from django.contrib import admin
from .models import CartItem, WishlistItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('product',)
    search_fields = ('user_username', 'product_name')

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('product',)
    search_fields = ('user__username', 'product__name')