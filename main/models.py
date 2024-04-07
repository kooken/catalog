from django.db import models

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

    def __str__(self):
        return f'{self.product_name} {self.product_description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)

