from importlib.resources import path

from staff.views import dashboard


from django.urls import path
from .views import dashboard

urlpatterns = [
    path("dashboard", dashboard, name="dashboard")
]