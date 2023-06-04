from django.shortcuts import render
from .models import Product_details_Model
# Create your views here.


def sample(r):
    prd_list = Product_details_Model.objects.all()
    prd_dict = {'prd_list': prd_list}

    return render(r,'connection/sample.html',context=prd_dict)


