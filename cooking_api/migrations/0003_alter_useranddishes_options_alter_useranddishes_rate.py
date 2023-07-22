# Generated by Django 4.2.2 on 2023-07-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking_api', '0002_useranddishes_dish_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useranddishes',
            options={'verbose_name': 'Лайк/Оценка', 'verbose_name_plural': 'Лайки/Оценки'},
        ),
        migrations.AlterField(
            model_name='useranddishes',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Очень плохо'), (2, 'Плохо'), (3, 'Средне'), (4, 'Хорошо'), (5, 'Отлично')], null=True, verbose_name='Рейтинг'),
        ),
    ]