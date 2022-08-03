from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from staff.models import *
from django.contrib import messages
import json

# Create your views here.


def home(request):
    products = Product.objects.filter(status = Product.LIVE)
    context = {
        "products": products
    }
    return render (request, "index.html",context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)


def shop(request):
    products = Product.objects.filter(status = Product.LIVE)
    context = {
        "products": products
    }
    return render (request, "shop.html",context)

def sign_in(request):
    context = {}
    return render(request, "sign_in.html", context)

def sign_up(request):
    context = {}
    return render(request, "sign_up.html", context)

def submitContactForm(request):

    if request.method == "POST":
    ## handle form data
      form_data =request.POST
      email = form_data["email"]
      name = form_data["name"]
      phone = form_data["phone"]
      message = form_data["message"]
 
      return HttpResponseRedirect("/form/success")
    
    else:
        return HttpResponseRedirect("/")
     
def successRedirect(request):
    context = {
     
    }

    return render(request, "success.html", context)    

def ajaxContactSubmission(request):
   
    email = request.POST["email"]
    name = request.POST["name"]
    number = request.POST["phone"]
    message = request.POST["message"]

    context = {
        "success": True,
        "message": "Thank you "+name+" for your message"
    }

    return JsonResponse(context)

def getProductDetails(request, id):

    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:

        messages.info("Sorry, that product does not exist")
        return HttpResponseRedirect("/")

    categories =Category.objects.all()
    all_products = Product.objects.exclude(pk=id)

    context = {
        "product":product,
        "categories": categories,
        "more_products": all_products
    }

    return render(request, "product-details.html", context) 

def searchProducts(request):

    query = request.POST["query"]

    products = Product.objects.filter(
        status = Product.LIVE).filter(name__contains=query).filter(
            category__contains = query
        )  
        

    context = {
        "products": products
    } 

    return render(request, "shop.html", context)    

def cart(request):
    context = {}
    return render(request, "cart.html", context)

def checkout(request):
    context = {}
    return render(request, "checkout.html", context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data ['productId']
    action = data['action']

    print('Action :', action)
    print('productId:', productId)
    
    customer = request.user.user_id
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer)
    orderItem, created = orderItem.objects.get_or_create(order=order, product=product) 

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
         orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if  orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse ('item was added', safe=False)