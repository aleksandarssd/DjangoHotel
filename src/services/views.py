from django.shortcuts import render

# Create your views here.
from .models import Services


def services(request):
    services = services.objects.all()
    context = {
        'services' : services
    }

    return render(request, context)