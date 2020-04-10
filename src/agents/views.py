from django.shortcuts import render

# Create your views here.
from .models import Agents


def agents_list(request):
    agents_list = Agents.objects.all()
    template = 'agents/list.html'
    context = {
        'agents_list' : agents_list
    }

    return render(request, template, context)