from django.db import models
from accounts.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    phone_verified = models.BooleanField(default=False)
