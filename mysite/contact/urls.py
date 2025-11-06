from django.urls import path
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    # path('', views.home, name = 'home'),
    path('', views.contact_view, name = 'contact'),
    path('success/', TemplateView.as_view(template_name = 'contact/success.html'), name= 'success')
]