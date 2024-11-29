from django.contrib import admin
from django.urls import path, include  # Use 'include' to link app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gas_service.urls')),  # Include URLs from the gas_service app
]
