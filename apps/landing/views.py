from django.shortcuts import render

from apps.catalog.models import Product
from apps.landing.models import AboutPage, ContactPage, MainPage


def main(request):
    context = dict()
    main_page = MainPage.objects.last()
    displayed_products = Product.objects.filter(is_on_home_page=True)
    context['products'] = displayed_products
    context['main_page'] = main_page
    return render(request, 'landing/main.html', context)


def about(request):
    about_page = AboutPage.objects.last()
    context = dict()
    context['about_page'] = about_page
    return render(request, 'landing/about.html', context)


def contact(request):
    contact_page = ContactPage.objects.last()
    context = dict()
    context['contact_page'] = contact_page
    return render(request, 'landing/contact.html', context)
