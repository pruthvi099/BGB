from django.forms import ModelForm
from customers.models import Customer


# Create the form class.
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "investment", "return_premium", "premium_day", "is_active"]