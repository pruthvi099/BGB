from premium.views import *
from django.urls import path

urlpatterns = [
    path('getall', GetAllPremium.as_view(), name='getall'),
    path('getprem', GetPremium.as_view(), name='getprem'),
]

appname = 'premium'