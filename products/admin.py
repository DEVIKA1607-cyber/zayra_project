from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Removed 'description' if not in model

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']  # Removed 'created_at' if not in model
    list_filter = ['category']  # Removed 'created_at' if not in model
    search_fields = ['name', 'description']
