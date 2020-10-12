from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=50000)
    publish_date = models.DateField()