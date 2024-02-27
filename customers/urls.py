from customers.views import *
from django.urls import path

urlpatterns = [
    path('manage', CustomerManage.as_view(), name='manage'),
    path('allview', CustomerView.as_view(), name='allview'),
]

appname = 'customers'
