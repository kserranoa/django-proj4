from django.urls import path
from .views import homepageview #import views

urlpatterns = [
    path('', homepageview.as_view()) #connect to views
]
