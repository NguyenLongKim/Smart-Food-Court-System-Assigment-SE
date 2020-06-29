from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomerUser(AbstractUser):
    name = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=10,default='')
    address = models.CharField(max_length=100,default='')
    school = models.CharField(max_length=100, default='')
    balance = models.FloatField(default=0)

    def __str__(self):
        return self.username