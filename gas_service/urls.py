from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home Page
    path('submit_request/', views.submit_request, name='submit_request'),  # Submit Service Request
    path('requests/', views.request_list, name='request_list'),  # List of Service Requests
    path('requests/<int:pk>/', views.request_detail, name='request_detail'),  # Request Detail
]
