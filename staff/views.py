from multiprocessing import context
from django.shortcuts import render

from staff.models import Product

# Create your views here.

def dashboard (request):
   

    context = {}

    return render (request, 'dashboard.html', context)

