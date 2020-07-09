from django.db import models
from .user import VendorOwner

class Vendor(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=256, default='')
    owner = models.ForeignKey(VendorOwner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name