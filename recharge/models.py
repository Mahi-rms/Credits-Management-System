from django.db import models
from app.models import User
# Create your models here.
class Recharge(models.Model):
    payment_id=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    amount=models.FloatField()
    paid_at=models.DateTimeField(blank=True,null=True)
    objects=models.Manager()