from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


# Create your views here.




def home(request):
    return HttpResponse("Welcome to my Django website!")


# def contact_view(request):
#     form = ContactForm()
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('success')
    #     else:
    #         render(request, 'contact/contact.html', {'form':form})
    # return render(request, 'contact/contact.html', {'form': form})




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('contact')  # redirect برای جلوگیری از resubmission
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})