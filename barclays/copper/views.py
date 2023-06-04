from django.shortcuts import render
from .models import CopperProduct

# Create your views here.

def index(r):
    prd = CopperProduct.objects.all()
    md = {'prd_list': prd}

    return render(r,'copper/index.html',context=md)
