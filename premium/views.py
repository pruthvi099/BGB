from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.db.models import Q, F

from premium.models import Premium
from customers.forms import CustomerForm

# Create your views here.

class GetAllPremium(View):
    template_name = 'premium/viewall.html'

    def get(self, request):
        allprem = list(Premium.objects.filter(is_paid=False).annotate(customerName=F('customer__name')).values())
        context = {
            'all_premiums':allprem
        }
        return render(request, self.template_name, context)

class GetPremium(View):
    template_name = 'premium/viewall.html'

    def get(self, request):
        id = request.GET.get('id', '')
        try: allprem = list(Premium.objects.filter(customer_id=id).annotate(customerName=F('customer__name')).values())
        except: allprem = []
        context = {
            'all_premiums':allprem
        }
        return render(request, self.template_name, context)

