from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib import messages

from apps.landing.models import AboutPage, ContactPage, MainPage, Image


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            messages.add_message(request, messages.ERROR, e.message)

        super().save_model(request, obj, form, change)


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            messages.add_message(request, messages.ERROR, e.message)

        super().save_model(request, obj, form, change)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            messages.add_message(request, messages.ERROR, e.message)

        super().save_model(request, obj, form, change)

