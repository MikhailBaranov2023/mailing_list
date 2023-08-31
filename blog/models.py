from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    body = models.TextField(verbose_name='содержимое')
    articles = models.TextField(verbose_name='статьи')
    image = models.ImageField(verbose_name='изображение')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    data = models.DateField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
