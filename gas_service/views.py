from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm

def home(request):
    return render(request, 'base.html')

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'request_form.html', {'form': form})

def request_list(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'request_list.html', {'requests': requests})

def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'request_detail.html', {'service_request': service_request})
