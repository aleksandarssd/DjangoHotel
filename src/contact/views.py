from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
from .models import ContactDetails
from django.core.mail import  BadHeaderError
from django.core.mail import send_mail as sm
from django.http import HttpResponse , HttpResponseRedirect






def send_mail(request):
    contactdetails = ContactDetails.objects.all()
    template = 'contact/contact.html'

    if request.method == 'POST' :
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            form_email = contact_form.cleaned_data['form_email']
            message = contact_form.cleaned_data['message']

            try :
                sm(subject , message , form_email , ['aleksandarrsd@gmail.com'])
            
            except BadHeaderError :
                return HttpResponse('invalid header')

            return redirect('contact:success')

    else:
        contact_form = ContactForm()    

    context = {
        'contactdetails' : contactdetails ,
        'contact_form' : contact_form
    }

    return render(request, template, context)


def success(request):
    return HttpResponse('Message Has been sent Successfully')


