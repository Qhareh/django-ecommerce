from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    context = {}
    return render (request, "index.html",context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)


def shop(request):
    context = {}
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