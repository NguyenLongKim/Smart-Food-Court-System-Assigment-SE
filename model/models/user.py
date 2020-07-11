from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type_account = models.CharField(max_length=50)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Customers'
        verbose_name_plural = 'Customers'


class VendorOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'VendorOwners'
        verbose_name_plural = 'VendorOwners'


class Cook(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    work_for = models.ForeignKey(VendorOwner, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cooks'
        verbose_name_plural = 'Cooks'


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Managers'
        verbose_name_plural = 'Managers'