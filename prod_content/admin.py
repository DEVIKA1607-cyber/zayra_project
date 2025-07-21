from django.contrib import admin
from .models import ProductImage, Review

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_url']
    search_fields = ['product__name']

