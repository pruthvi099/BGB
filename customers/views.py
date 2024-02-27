from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse

from customers.models import Customer
from customers.forms import CustomerForm

# Create your views here.

class CustomerView(View):
    template_name = 'customers/viewall.html'
    
    def get(self, request):
        allCust = list(Customer.objects.filter(name='Siddhart').values())
        context = {
            'all_customers':allCust
        }
        return render(request, self.template_name, context)
    
class CustomerManage(View):
    template_name = 'customers/createadd.html'
    
    def get(self, request):
        id = request.GET.get('id', '')
        
        try: 
            cust = Customer.objects.filter(id=id)
            if cust.exists():
                cust = cust[0]
            else:
                cust = {}
        except: cust = {}

        form = CustomerForm(initial=cust)

        context = {
            'all_customers':cust,
            'form':form,
            # 'post_url': reverse('customers:customerManage')
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        id = request.GET.get('id', '')

        form = CustomerForm(request.POST)

        if form.is_valid():
            cust = form.save()
        
            try: 
                cust = Customer.objects.filter(id=cust.id)
                if cust.exists():
                    cust = cust[0]
                else:
                    cust = {}
            except: cust = {}
            msg = "Added Sucessfully"
        else: 
            msg = form.errors


        context = {
            'cust':cust,
            'form':form,
            'msg':msg,
        }

        return render(request, self.template_name, context)