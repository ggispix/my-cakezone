from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import OurService
def index(request):
    services = OurService.objects.filter(is_visible=True)
    context = {
        'services': services
    }
    return render(request, 'services.html', context=context)