from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Category, Product


def category_overview(request, slug):
    if not Category.objects.filter(slug=slug).exists():
        return Http404()
    category = Category.objects.filter(slug=slug).first()
    products = Product.objects.filter(category=category, is_hidden=False)

    page_num = request.GET.get('page', 1)
    paginator = Paginator(products, 27)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = dict()
    context['category'] = category
    context['page_obj'] = page_obj
    return render(request, 'catalog/category_overview.html', context=context)


def search_product(request, slug):
    page_num = request.GET.get('page', 1)
    if 'query' in request.POST:
        query = request.POST['query'].lower()
    else:
        query = request.GET['query'].lower()
    products = []
    category = Category.objects.filter(slug=slug).first()
    for product in Product.objects.filter(category=category, is_hidden=False):
        title = product.title.lower()
        if query in title:
            products.append(product)
    paginator = Paginator(products, 27)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = dict()
    context['category'] = category
    context['page_obj'] = page_obj
    context['query'] = query
    return render(request, 'catalog/category_search.html', context=context)


def product_overview(request, category_slug, product_slug):
    if not Product.objects.filter(slug=product_slug, is_hidden=False).exists():
        return Http404()

    product = Product.objects.filter(slug=product_slug).first()
    context = dict()
    context['product'] = product
    return render(request, 'catalog/product_overview.html', context=context)


