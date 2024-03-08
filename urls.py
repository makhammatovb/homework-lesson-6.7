from django.urls import path

from .views import index, about, contact, services, staff

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('staff/', staff, name='staff'),
]