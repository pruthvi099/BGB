from django.db import models
from customers.models import Customer

# Create your models here.

class Premium(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    
    amount = models.IntegerField(default=0)
    is_paid = models.BooleanField(blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
