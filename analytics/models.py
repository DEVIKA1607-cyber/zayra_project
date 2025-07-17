from django.db import models
from products.models import Product

class Analytics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    daily_views = models.IntegerField(default=0)
    cart_count = models.IntegerField(default=0)
    orders_count = models.IntegerField(default=0)
    search_terms = models.TextField(blank=True)
