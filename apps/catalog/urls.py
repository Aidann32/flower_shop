from django.urls import path

from .views import *

urlpatterns = [
    path('<str:slug>', category_overview, name='category_overview'),
    path('<str:slug>/search', search_product, name='search_product'),
    path('<str:category_slug>/<str:product_slug>', product_overview, name='product_overview'),
]