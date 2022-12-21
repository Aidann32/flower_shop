from django.db import models
from apps.catalog.tools import slugify

from django_quill.fields import QuillField


class Category(models.Model):
    title = models.CharField('Название категории', max_length=255)
    description = QuillField('Описание категории', null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True, verbose_name='Слаг(название в ссылке)', help_text='Если слаг не будет указан, он будет заполнен автоматически')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField('Название товара', max_length=255)
    description = QuillField('Описание товара', null=True, blank=True)
    is_on_home_page = models.BooleanField('Будет ли данный продукт отображаться на главной', default=False)
    is_hidden = models.BooleanField('Скрыть продукт', default=False)
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2, default=0.0)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True, verbose_name='Слаг(название в ссылке)', help_text='Если слаг не будет указан, он будет заполнен автоматически')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.category.title}: {self.title}'

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def get_cover_image(self):
        cover_image = self.image_set.filter(is_cover=True).first()
        if not cover_image:
            cover_image = self.image_set.first()
        return cover_image

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    image = models.ImageField('Картинка', upload_to='product_images/')
    is_cover = models.BooleanField('Обложка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

