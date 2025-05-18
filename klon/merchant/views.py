from django.shortcuts import render
from .models import Merchant

def merchant_list(request):
    merchants = Merchant.objects.all()
    return render(request, 'merchant/merchant_list.html', {'merchants': merchants})




