from django.db import models

# Create your models here.
NULLABLE = {'null': True,
            'blank': True}
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='posts/', verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'