from django.db import models

# Create your models here.
# academy_app/models.py

from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment of {self.amount} for {self.user.username}"
