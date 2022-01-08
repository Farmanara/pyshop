''' models '''
from django.db import models

class Product(models.Model):
    ''' products attributes '''
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)

    def __str__(self):
        return self.name

class Offer(models.Model):
    ''' discounts model '''
    code=models.CharField(max_length=7)
    description=models.CharField(max_length=100)
    discount=models.FloatField()

    def __str__(self):
        return "Coupon"
