from django.contrib import admin

from .models import Category, Product, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title', 'description', ]
    list_display = ('title', 'get_price', 'category', 'is_on_home_page_display', 'is_hidden_display')
    list_filter = ('category', 'is_on_home_page', )

    def is_on_home_page_display(self, obj):
        if obj.is_on_home_page:
            return True
        return False
    is_on_home_page_display.short_description = 'На главной'
    is_on_home_page_display.boolean = True

    def is_hidden_display(self, obj):
        if obj.is_hidden:
            return True
        return False
    is_hidden_display.short_description = 'Скрыт'
    is_hidden_display.boolean = True

    def get_price(self, obj):
        return f'{obj.price} ₸'
    get_price.short_description = 'Цена'
