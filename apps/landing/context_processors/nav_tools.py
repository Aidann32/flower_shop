from apps.catalog.models import Category
from apps.landing.models import MainPage


def get_categories(request):
    return {'all_categories': Category.objects.all() }


def get_main_page(request):
    return {'main_page': MainPage.objects.first()}
