from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import ContactForm
# Create your views here.




def home(request):
    return HttpResponse("Welcome to my Django website!")


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            render(request, 'contact/contact.html', {'form':form})
    return render(request, 'contact/contact.html', {'form': form})




