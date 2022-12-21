from django.core.exceptions import ValidationError
from django.db import models
from django_quill.fields import QuillField


class MainPage(models.Model):
    content = QuillField(null=True, blank=True, verbose_name='Контент', help_text='Может быть только один экземпляр!')
    banner_title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Заголовок в банере')
    banner_description = models.CharField(max_length=100, null=True, blank=True, verbose_name='Описание в банере')

    wp_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Номер WhatsApp', help_text='Формат номера +770570570723')
    wp_text = models.CharField(max_length=500, null=True, blank=True, verbose_name='Текст для WhatsApp')

    def __str__(self):
        return 'Главная страница'

    def save(self, *args, **kwargs):
        if not MainPage.objects.filter(pk=self.pk).exists() and MainPage.objects.exists():
            raise ValidationError('Может только один экземпляр!')
        return super(MainPage, self).save(*args, **kwargs)

    def get_image_url(self):
        if not self.image_set.exists():
            return None
        return self.image_set.last().image.url

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Image(models.Model):
    image = models.ImageField('Картинка на слайдере', upload_to='main_page_slider_images/')
    main_page = models.ForeignKey(MainPage, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка на слайдере'
        verbose_name_plural = 'Картинки на слайдере'


class ContactPage(models.Model):
    content = QuillField(null=True, blank=True, verbose_name='Контент', help_text='Может быть только один экземпляр!')

    def __str__(self):
        return 'Страница "Контакты"'

    def save(self, *args, **kwargs):
        if not ContactPage.objects.filter(pk=self.pk).exists() and ContactPage.objects.exists():
            raise ValidationError('Может только один экземпляр!')
        return super(ContactPage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страница "Контакты"'
        verbose_name_plural = 'Страница "Контакты"'


class AboutPage(models.Model):
    content = QuillField(null=True, blank=True, verbose_name='Контент', help_text='Может быть только один экземпляр!')

    def __str__(self):
        return 'Страница "О нас"'

    def save(self, *args, **kwargs):
        if not AboutPage.objects.filter(pk=self.pk).exists() and AboutPage.objects.exists():
            raise ValidationError('Может только один экземпляр!')
        return super(AboutPage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Страница "О нас"'
        verbose_name_plural = 'Страница "О нас"'

