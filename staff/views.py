from multiprocessing import context
from django.shortcuts import render

from staff.models import Product, Category, Review

# Create your views here.

def dashboard(request):

    total_categories = Category.objects.count()
    total_products =Product.objects.count()
    review = Review.objects.all()

    context = {

        "total_products": total_products,
        "total_categories": total_categories,
        "messages": review
    }

    return render (request, "dashboard.html", context)

def categories(request):

    categories = Category.objects.all() 

    context = {
        "categories" : categories
    } 

    return render(request, "category.html", context)

def products(request):

    products = Product.objects.all()

    context = {
        "products" : products
    }  

    return render(request, "product.html", context) 

def reviews(request):

    messages = Review.objects.all()

    return render(request, "review.html", {'messages': messages}) 
