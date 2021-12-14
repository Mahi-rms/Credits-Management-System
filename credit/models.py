from django.db import models
# Create your models here.
class Credit(models.Model):
    payment_id=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    amount=models.FloatField()
    transaction_type=models.CharField(max_length=255)
    paid_at=models.DateTimeField(blank=True,null=True)
    valid_upto=models.DateTimeField(blank=True,null=True)
    objects=models.Manager()