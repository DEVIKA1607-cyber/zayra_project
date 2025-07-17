from django.contrib import admin
from .models import Analytics  # Model from models.py

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('product', 'daily_views', 'cart_count', 'orders_count')
    search_fields = ('product__name',)
