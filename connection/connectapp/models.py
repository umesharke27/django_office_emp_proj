from django.db import models

# Create your models here.

class Product_details_Model(models.Model):
    name = models.CharField(max_length=25)
    prd_qnty = models.IntegerField()
    prd_price = models.FloatField()
    prd_loc=models.CharField(max_length=10)




