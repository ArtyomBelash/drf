from django.db import models


class Dish(models.Model):
    title = models.CharField('Заголовок', max_length=140)
    recipe = models.TextField('Рецепт')
    created = models.DateTimeField('Дата', auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', related_name='dish')
    images = models.ManyToManyField('DishImage', blank=True, related_name='dishes')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField('Категория', max_length=140)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class DishImage(models.Model):
    image = models.ImageField('Фото', upload_to='food_image', blank=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
