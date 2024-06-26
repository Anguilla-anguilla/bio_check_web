from django.db import models


class FoodAdditives(models.Model):
    e_title = models.CharField(max_length=125, verbose_name='номер добавки')
    common_title = models.CharField(max_length=125, verbose_name='название')
    category = models.CharField(max_length=125, verbose_name='категория')
    description = models.TextField(verbose_name='описание')
    is_dangerous = models.BooleanField(verbose_name='опасна', default=False)
    is_informative = models.BooleanField(
        verbose_name='есть информация по добавке',
        default=True
        )

    class Meta:
        verbose_name = 'объект "пищевая добавка"'
        verbose_name_plural = 'Пищевые добавки'

    def __str__(self):
        title = self.e_title
        return title
