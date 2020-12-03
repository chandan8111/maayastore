from django.db import models
from datetime import datetime


# All product models
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    product_desc = models.TextField(max_length=10000)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="shop/images", default="")
    publish_date = models.DateField()

    def __str__(self):
        return self.product_name


# Contact Page Models
class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default="")
    desc = models.TextField(max_length=5000, default="")

    def __str__(self):
        return self.name


# Order product delivery details models
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(default=datetime.now(), blank=True)
    items_json = models.TextField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.TextField(max_length=2000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15, default="")


# Ordered product tracking modules
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.TextField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:50] + "..."
