from importlib.resources import path

from staff.views import dashboard


from django.urls import path
from .views import categories, dashboard, products, reviews

urlpatterns = [
    path("dashboard", dashboard, name="dashboard"),
    path("categories", categories, name="categories"),
    path("products", products, name="products"),
    path("reviews", reviews, name="reviews"),
]