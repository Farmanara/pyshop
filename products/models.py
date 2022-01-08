''' models '''
from django.db import models

class Product(models.Model):
    ''' products attributes '''
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)

class Offer(models.Model):
    ''' discounts model '''
    code=models.CharField(max_length=7)
    description=models.CharField(max_length=100)
    discount=models.FloatField()
