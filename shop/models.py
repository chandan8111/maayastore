from django.db import models

# All product models
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    product_desc = models.CharField(max_length=10000)
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
    desc = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.name