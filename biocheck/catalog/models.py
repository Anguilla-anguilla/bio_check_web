from django.db import models


class FoodAdditives(models.Model):
    e_title = models.IntegerField()
    common_title = models.CharField(max_length=125)
    category = models.CharField(max_length=125)
    description = models.TextField()
    is_dangerous = models.BooleanField()