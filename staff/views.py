from itertools import product
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from staff.models import Product, Category, Review
from staff.forms import CategoryForm, ReplyFeedbackForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
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

def createCategory(request):

    if request.method == "GET":
        form = CategoryForm()
        action = "Create" 

        context = {

            "action": action,
            "form": form
        }  

        return render(request, "category-form.html", context)    

    else:

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/staff/categories')  

def deleteCategory(request, id):

    category = Category.objects.filter(pk=id).first()
    category.delete()

    data = {
        "success": True
    }

    return JsonResponse(data)   

## Class based Views
class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "product.html" 

class ProductCreateView(CreateView):
    model= Product
    success_url = "/staff/products"
    template_name ="product-form.html"
    #fields = '__all__'
    fields = ["name", "image", "price", "description", "category", "quantity", "status"] 

class ProductUpdateView(UpdateView):
    model= Product
    success_url = "/staff/products"
    template_name ="product-form.html"
    #fields = '__all__'
    fields = ["name", "image", "price", "description", "category", "quantity", "status"] 
    
def deleteProduct(request, id):

    try:
        product = Product.objects.get(pk=id)  

    except Product.DoesNotExist:

        return JsonResponse({"success": False})

    product.delete()

    data = {
        "success": True
    } 

    return JsonResponse(data)   