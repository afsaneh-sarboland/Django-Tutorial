from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

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
    form = ContactForm(request.POST or None)
    success = False
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(subject=f"New message from {name}",
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=['sarboland.afsaneh@gmail.com'],
                  fail_silently=False
                  )
        success = True
        form = ContactForm() #reset the form
        return render(request, 'contact/contact.html', {'form': form,'success':success})
    return render(request, 'contact/contact.html', {'form':form})