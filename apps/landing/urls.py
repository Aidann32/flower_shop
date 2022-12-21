from django.urls import path
from .views import main, about, contact

urlpatterns = [
    path('', main, name='main_page'),
    path('about', about, name='about_page'),
    path('contact', contact, name='contact_page')
]