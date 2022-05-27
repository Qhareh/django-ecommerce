from itertools import product
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(User):
    address = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Category(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
        return self.name

class Product(models.Model):
    LIVE = 1
    OUT_OF_STOCK = 2
    PENDING = 3

    PRODUCT_STATUS = (
        (LIVE, "Live"),
        (OUT_OF_STOCK, "Out of Stock"),
        (PENDING, "Pending")
    )
    name = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    status = models.IntegerField(choices= PRODUCT_STATUS, default= LIVE)

    def __str__(self):
        return self.name


class Review(models.Model):
    ratings = models.IntegerField(default=0)
    feedback = models.TextField(null=True, blank=True)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.product.name +": "+str(self.ratings)

class Order(models.Model):
    total = models.FloatField()   
    order_number = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number 

class CartProduct(models.Model):
    quantity = models.IntegerField(default=1)
    product =   models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.FloatField()
    order =models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.name


class Payment(models.Model):
    CASH = 0
    MPESA = 1

    PAYMENT_METHOD = (
        (CASH, "Cash"),
        (MPESA, "M-pesa")
    )

    method= models.IntegerField(choices=PAYMENT_METHOD, default= MPESA)
    total = models.FloatField()
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    reference_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.reference_number

