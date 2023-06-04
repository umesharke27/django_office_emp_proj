from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(r):

    return render(r,'loan/loan.html')

#def view(r):
    #return HttpResponse('<h1> this is view page </h1>')

#def home(r):
   # return HttpResponse('<h1> this is home page </h1>')