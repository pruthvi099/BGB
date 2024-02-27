from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)

    is_active = models.BooleanField(blank=True, null=True)
    investment = models.IntegerField(default=0)
    return_premium = models.IntegerField(default=0)
    premium_day = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
