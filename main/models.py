from django.db import models

from users.models import User

# Create your models here.

NULLABLE = {'null': True,
            'blank': True}

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_description = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.CharField(max_length=200, verbose_name='описание')
    product_image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.product_name} {self.product_description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)



class Version(models.Model):
    # product = models.CharField(max_length=100, verbose_name='продукт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='version',
                                verbose_name='наименование')
    version_no = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    active_version = models.BooleanField(default=True, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'



