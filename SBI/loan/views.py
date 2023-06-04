from django.shortcuts import render

# Create your views here.

def home_loan(r):
    return render(r,'loan/home.html')

def personal_loan(r):
    return render(r,'loan/personal.html')

def business_loan(r):
    return render(r,'loan/business.html')
