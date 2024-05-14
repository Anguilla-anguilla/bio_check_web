from django.db import models


class FoodAdditives(models.Model):
    e_title = models.IntegerField(verbose_name='номер E')
    common_title = models.CharField(max_length=125, verbose_name='название')
    category = models.CharField(max_length=125, verbose_name='категория')
    description = models.TextField(verbose_name='описание')
    is_dangerous = models.BooleanField(verbose_name='опасна')

    class Meta:
        verbose_name = 'пищевая добавка'
        verbose_name_plural = 'Пищевые добавки'

    def __str__(self):
        return self.e_title