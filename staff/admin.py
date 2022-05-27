from django.contrib import admin

from staff.models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(CartProduct)
