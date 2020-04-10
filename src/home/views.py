from django.shortcuts import render
from property.models import Property, Category
from agents.models import Agents
from services.models import Services
from django.db.models import Count
# Create your views here.






def home(request):
    category_list = Category.objects.annotate(property_count=Count('property')).values('category_name', 'property_count', 'image')
    property_list = Property.objects.all()
    agent_list = Agents.objects.all()
    services_list = Services.objects.all()
    template = 'home/home.html'
    context = {
        'category_list_home' : category_list,
        'property_list_home' : property_list,
        'agent_list_home': agent_list,
        'services_list': services_list,
        
    }

    return render(request, template, context)