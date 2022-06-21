from importlib.resources import path

from staff.views import dashboard


from django.urls import path
from .views import *
urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("categories", categories, name="categories"),
    path("products", products, name="products"),
    path("reviews", reviews, name="reviews"),
    path("create/category/", createCategory, name="create.category"),
    path("delete/category/<id>", deleteCategory, name="delete.category"),
    path("products", ProductListView.as_view(), name="products"),#Class Based View
    path("create/product", ProductCreateView.as_view(), name="product.create"),
    path("update/product/<pk>", ProductUpdateView.as_view(), name="update.product"),
    path("delete/product/<id>", deleteProduct, name= "delete.product"),
]