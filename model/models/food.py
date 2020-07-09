from django.db import models
from .vendor import Vendor

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=256)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='food_images/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Foods'
        verbose_name_plural = 'Foods'