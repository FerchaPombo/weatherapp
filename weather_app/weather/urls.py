from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.home, name='home'),  # Refer to the home function from views module
]