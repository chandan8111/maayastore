from django.db import models


# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100, default="")
    sub_category = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=500)
    publish_date = models.DateTimeField()
    heading0 = models.CharField(max_length=500, default="")
    Con_heading0 = models.TextField(max_length=10000, default="")
    heading1 = models.CharField(max_length=500, default="")
    Con_heading1 = models.TextField(max_length=20000, default="")
    sub_heading = models.CharField(max_length=500, default="")
    Con_sub_heading = models.TextField(max_length=30000, default="")
    thumbnail = models.ImageField(upload_to='blog/thumbnail', default="")

    def __str__(self):
        return self.title
