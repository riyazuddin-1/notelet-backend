from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class OTP(models.Model):
    email = models.EmailField()
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self, expiry_minutes=10):
        return timezone.now() - self.created_at < timedelta(minutes=expiry_minutes)